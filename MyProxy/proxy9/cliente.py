# -*- coding: utf-8 -*-
import socket
import time

data = time.ctime()

log = open("log.txt", "w")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 3128))

while True:
    mensagem = input("Mensagem: ")

    if mensagem == "block":
        cliente.close()

    if mensagem == "proxy":
        print("ERROR 404 - Xandão Fela da Puta")
        log.writelines(['ERROR 404', data, '\n'])

    cliente.send(mensagem.encode())
    mensagem = cliente.recv(1024)
    msg = mensagem.decode()
    if msg == "hora":
        print(data, " : ")
    print(msg)