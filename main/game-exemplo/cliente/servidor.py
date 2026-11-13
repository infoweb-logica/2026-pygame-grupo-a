import socket
import random

servidor = None

def conectar(cor):
    global servidor
    # Configuração do cliente
    host = "10.25.2.225"
    porta = 8004
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.connect((host, porta))
    servidor.sendall(f"NOVO,{random.randint(0, 255)},{cor}".encode("utf-8"))  # Envia uma mensagem para o servidor indicando que um novo jogador se conectou

def enviar_posicao(x, y):
    global servidor
    # Envia a posição do jogador para o servidor
    posicao = f"{x},{y}"
    servidor.sendall(posicao.encode("utf-8"))

def novo_jogador():
    global servidor
    # Envia uma mensagem para o servidor indicando que um novo jogador se conectou
    mensagem = "NOVO_JOGADOR"
    jogador = servidor.recv(1024)  # Recebe a resposta do servidor