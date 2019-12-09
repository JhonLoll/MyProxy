# -*- coding: utf-8 -*-
import socket
import time

data = time.ctime()

log = open("log.txt", "a")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 3128))

while True:
    mensagem = input("Mensagem: ")

    # if mensagem == "block":
    #     cliente.close()
    #     log.writelines(['Mensagem não permitida, fechando conexão', data, '\n'])

    if mensagem == "proxy":
        print("ERROR 404 - Xandão Fela da Puta")
        log.writelines(['ERROR 404', data, '\n'])

    cliente.send(mensagem.encode())
    mensagem = cliente.recv(1024)
    msg = mensagem.decode()

    log.writelines(['Recebido: ', msg, ' : ',data])
    log.close()

    if msg == "hora":
        print(data, " : ")
    print(msg)