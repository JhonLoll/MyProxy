import socket
import time

data = time.ctime()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.106"
port = 3129

ip = (host, port)

server.bind(ip)
server.listen(5)

print("SERVIDOR INICIADO", (ip))

log = open("log.txt", "w")
log.writelines(['Servidor Iniciado: ', data, '\n'])
log.close()

while True:

    client, ipclient = server.accept() 
    print("Conectado por: ", ipclient)

    mensagem = client.recv(2048)
    msg = mensagem.decode()
    print(data, " : ",msg)

    client.send(bytes(msg, 'utf-8'))

    if msg == True:
        log.writelines(['Recebido: ', msg,' : ', data])
        log.close()

    if msg == "block":
        client.send(bytes("Fechando", 'utf-8'))
        log.writelines(['ERROR 404', data])
        log.close()
        client.close()
        break