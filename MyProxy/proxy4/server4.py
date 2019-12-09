import socket
from threading import *
import time

host = "localhost"
port = 3128

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((host, port))

print("========== SERVIDOR INICIADO ==========\n\n","Data : ", time.ctime(),"\n\n", "Na porta: ", host," : ",port, "\n\n ====================================")

cliente = server.recvfrom(3128)

cliente[0]

print("Conectado por: %s" %cliente[0])

while True:

    msgs = message.recvfrom(2048)

    msg = msgs.decode("utf-8").upper()

    server.sendto(msg.encode("utf-8"), cliente)

    print("Hora: ", time.ctime()," : ",msg)