import socket
import time

host = "localhost"

port = 3128

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))

server.listen(5)

print("Servidor iniciado em: ", time.ctime(),"Na porta -> ", host, ":", port)

while True:
    conn, end = server.accept()
    print("Server conectado por: ", end)

    while True:
        data = conn.recv(1024)

        if not data: break

        conn.send(b'Echo=>' + data)

        