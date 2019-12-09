import socket
import time

data = time.ctime()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.28.1"
port = 3130

ip = (host, port)

server.bind(ip)
server.listen(5)

print("SERVIDOR INICIADO", (ip))

log = open("log.txt", "a")

log.writelines(['Servidor Iniciado: ', data, '\n'])


while True:

    client, ipclient = server.accept() 
    print("Conectado por: ", ipclient)

    if ipclient == "":
        print("CLIENTE BLOQUEADO")
        log.writelines(['CONEXÃO BLOQUEADA', str(ipclient)])

    mensagem = client.recv(2048)
    msg = mensagem.decode()
    print(data, " : ",msg)

    client.send(bytes(msg, 'utf-8'))

    if msg == True:
        log.writelines(['Recebido: ', msg,' : ', data])

    if msg == "block":
        print("ENCERRANDO CONEXÃO...", (ipclient))
        log.writelines(['Conexão Encerrada', data])
        client.close()
        break

log.close()