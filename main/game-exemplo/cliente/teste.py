import socket

# Configuração do cliente
host = "192.168.56.1"
porta = 8001

# Cria o socket e conecta ao servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, porta))

# Envia uma mensagem
mensagem = "Olá, servidor! Conectado via socket puro em Python."
cliente.sendall(mensagem.encode("utf-8"))

# Recebe a resposta do servidor
resposta = cliente.recv(1024)
print(f"[RESPOSTA DO SERVIDOR]: {resposta.decode('utf-8')}")

# Fecha a conexão
cliente.close()