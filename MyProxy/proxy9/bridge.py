import socket
import time

data = time.ctime()

bridge = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 3128

ip = (host, port)
bridge.bind(ip)

bridge.listen(5)

print("PONTE INICIADA")

while True:
    client, ipclient = bridge.accept()
    mensagem = client.recv(2048)
    msg = mensagem.decode()
    print("Mensagem enviada para o servidor: \n",">>>",msg)
    
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("192.168.1.106", 3129))
    conn.send(msg.encode())

    resposta = conn.recv(1024)
    client.send(bytes(resposta))
    print("Resposta ao cliente: \n",">>>",resposta)
