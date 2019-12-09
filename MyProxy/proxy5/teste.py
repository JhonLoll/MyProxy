import socket
from os import system

ip = "0.0.0.0"
port = 3128

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((ip, port))

    server.listen(5)

    print("Iniciado em %s %s" %(ip, port))

    (obj, cliente) = server.accept()

    print("Conexão de %s" %cliente[0])

    while True:

        msg = obj.recvfrom(1024)
        msg = msg[-1]
        if msg == 'ls':
            system(ls)
        if msg == 'local':
            system('pwd')
        if msg == '':
            print(msg)
        else: 
            print("Comando Invalido")

        server.close()

except Exception as erro:
    print(erro)
    server.close()