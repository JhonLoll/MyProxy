import socket
import time

host = "0.0.0.0"
port = 3128

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

print("Servidor iniciado em: ", time.ctime(),"Na porta -> ", host, ":", port)

clients = []
while True:
    data, addr = s.recvfrom(1024)
    text = data.decode('utf-8')
    if "Quit" in text:
        break

    if addr not in clients:
        clients.append(addr)

    print(time.ctime(), "-", addr, ":", text)
    for client in clients:
        s.sendto(data, client)

s.close()