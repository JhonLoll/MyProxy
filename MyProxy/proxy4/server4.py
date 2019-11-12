import socket
from threading import *

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("localhost", 3128))

while True:

    msgs, endCliente = server.recvfrom(2048)

    msg = msgs.decode("utf-8").upper()

    server.sendto(msg.encode("utf-8"), endCliente)

    print(msg)