import socket
import time

data = time.ctime()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 3128))

while True:
    msg = input("Digite a mensagem: ")
    if msg == "xande":
        print("bloqueado")
        client.close()
        break
    client.send(msg.encode())
    mensagem = client.recv(2048)
    
    msgs = mensagem.decode()
    if msgs == "hora":
        print(data, " : ", msg)

    print(msgs)
