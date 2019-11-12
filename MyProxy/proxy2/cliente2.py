import socket
import threading

serverHost = 'localhost'
serverPort = 3128

mensagem = ("Olá Cliente", 'utf-8')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((serverHost, serverPort))

for linha in mensagem:
    server.send(linha)

    data = server.recv(1024)
    print("Cliente Recebe", data)