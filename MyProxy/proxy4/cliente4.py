import socket
from threading import *

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    mensagem_envio = input("Digite a mensagem: ")
    cliente.sendto(msg.encode("utf-8"),("localhost", 3128))

    msgs, endServer = cliente.recvfrom(2048)

    print(msgs.decode("utf-8"))