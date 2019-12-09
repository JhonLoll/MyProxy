import socket  
import time 

proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = "localhost"
port = 3128

proxy.bind((host, port))
proxy.listen(5)

print("PONTE INICIADA")
while True:
    client, ipCliente = proxy.accept()
    mensagem = client.recv(2048)

    msg = mensagem.decode()

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.connect(("192.168.1.106", 3129))
    serv.send(msg.encode())

    resposta = serv.recv(1024)
    client.send(bytes(resposta))