import socket
import threading
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("localhost", 3127))

sock.listen(1)

servers = []

print("INICIADO")

def handler(c, a):
    global servers
    while True:
        data = c.recv(1024)
        for conectados in servers:
            conectados.send(bytes(data))
        if not data:
            servers.remove(c)
            c.close()
            break
        if (bytes(data)) == "oi":
            servers.remove(c)
            sock.close()
            break
while True:
    c, a = sock.accept()

    cThread = threading.Thread(target=handler, args=(c,a))

    cThread.daemon = True

    cThread.start()

    # servers.append(c)

    # print(servers)