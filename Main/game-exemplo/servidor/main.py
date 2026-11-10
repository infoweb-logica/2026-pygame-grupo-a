import socket
import threading

class Jogador:
    def __init__(self, conexao, endereco, nome, cor):
        self.conexao = conexao
        self.endereco = endereco
        self.nome = nome
        self.cor = cor
        self.posicao = (0, 0)  # Posição inicial do jogador

jogadores = []

def jogador(conexao, endereco):
  while True:
    conteudo = conexao.recv(1024).decode("utf-8")
    if conteudo:
      mensagem = conteudo.split(",")
      if mensagem[0] == "NOVO":
        jogador_novo = Jogador(conexao, endereco, f"Jogador{len(jogadores)+1}", (int(mensagem[1]), int(mensagem[2]), int(mensagem[3])))
        jogadores.append(jogador_novo)
      print(f"[POSIÇÃO RECEBIDA] Do jogador {endereco}: {conteudo}")
  conexao.close()  # Fecha a conexão com o cliente quando ele desconectar

def iniciar_servidor():
  # 1. Cria o socket (AF_INET = IPv4, SOCK_STREAM = TCP)
  servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Permite reutilizar o endereço IP/porta imediatamente após fechar
  servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  # 2. Define o endereço (IP) e a porta
  # Usar 'localhost' ou '127.0.0.1' significa que apenas sua máquina conecta
  # Usar '' (string vazia) aceita conexões de qualquer IP na rede local
  host = "10.25.2.225"
  porta = 8004

  # 3. Associa o socket ao host e à porta
  servidor.bind((host, porta))

  # 4. Coloca o servidor em modo de escuta (o número 30 é o limite de conexões em espera)
  servidor.listen(30)
  print(f"[SERVIDOR] Escutando em {host}:{porta}...")

  try:
    while True:
      # 5. Aceita a conexão de um cliente (bloqueia até alguém conectar)
      conexao_cliente, endereco_cliente = servidor.accept()
      print(f"[CONEXÃO] Conectado com sucesso ao cliente: {endereco_cliente}")
      threading.Thread(target=jogador, args=(conexao_cliente, endereco_cliente)).start()  # Cria uma nova thread para lidar com o jogador conectado

  except Exception as e:
    print(f"[ERRO] Ocorreu um erro: {e}")
    conexao_cliente.close()  # Fecha a conexão com o cliente em caso de erro
  except KeyboardInterrupt:
    print("\n[SERVIDOR] Servidor encerrado manualmente.")
  finally:
    servidor.close()


if __name__ == "__main__":
  iniciar_servidor()