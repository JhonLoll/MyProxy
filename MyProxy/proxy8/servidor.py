import socket 
import time 

data = time.ctime()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = "192.168.1.106"
port = 3129

server.bind((host, port))

server.listen(5)

print("SERVIDOR INICIADO")

while True:

    client, ipClient = server.accept()
    msg = client.recv(2048)

    mensagem = msg.decode()

    print("Conectado por: ", ipClient)
    print(data, " : ", mensagem)

    client.send(bytes(mensagem, 'utf-8')) 

        