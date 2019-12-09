import socket
from threading import *

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    msgs = input("Digite a mensagem: ")
    cliente.sendto(msgs.encode("utf-8"),("localhost", 3128))

    msgs, endServer = cliente.recvfrom(2048)

    print(msgs.decode("utf-8"))