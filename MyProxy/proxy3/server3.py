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

    message, endCliente = s.recvfrom(2048)

    message = message.decode("utf-8").upper()

    s.sendto(message.encode("utf-8"), endCliente)

    print("Hora: ", time.ctime()," : ", message)

    log = open("log1.txt", "w")
    log = open("arq01.txt", "w")

    log.write("Servidor Iniciado em: ")
    log.write(time.ctime())
    log.write("Recebido: ")


    data, addr = s.recvfrom(1024)
    text = data.decode('utf-8')

    log.write(text)

    if addr == "192.168.28.1":
        break

    if "Quit" in text:
        break
    if "ls" in text:
        print('ARQUIVOS')

    if addr not in clients:
        clients.append(addr)

    print(time.ctime(), "-", addr, ":", text)
    for client in clients:
        s.sendto(data, client)

s.close()