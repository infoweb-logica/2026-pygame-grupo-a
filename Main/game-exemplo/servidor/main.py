import socket

def iniciar_servidor():
  # 1. Cria o socket (AF_INET = IPv4, SOCK_STREAM = TCP)
  servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Permite reutilizar o endereço IP/porta imediatamente após fechar
  servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  # 2. Define o endereço (IP) e a porta
  # Usar 'localhost' ou '127.0.0.1' significa que apenas sua máquina conecta
  # Usar '' (string vazia) aceita conexões de qualquer IP na rede local
  host = "192.168.56.1"
  porta = 8001

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

      # 6. Recebe os dados enviados pelo cliente (tamanho máximo do buffer: 1024 bytes)
      dados_recebidos = conexao_cliente.recv(1024)

      if dados_recebidos:
        mensagem = dados_recebidos.decode("utf-8")
        print(f"[MENSAGEM RECEBIDA] {mensagem}")

        # 7. Envia uma resposta de volta ao cliente
        resposta = "Mensagem recebida com sucesso pelo servidor!"
        conexao_cliente.sendall(resposta.encode("utf-8"))

      # 8. Fecha a conexão com este cliente específico
      conexao_cliente.close()
      print(f"[CONEXÃO] Conexão encerrada com {endereco_cliente}\n")

  except KeyboardInterrupt:
    print("\n[SERVIDOR] Servidor encerrado manualmente.")
  finally:
    servidor.close()


if __name__ == "__main__":
  iniciar_servidor()