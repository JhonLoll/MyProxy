import socket
import time

ip = "10.1.2.104"
host = 3125

r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    r.bind((ip, host))

    r.listen(1)

    print("Server Resposta Iniciado %s %s" %(ip, host))

    (message, bridge) = r.accept()

    print("Ponte Feita com:  %s" %bridge[0])

    while True:

        resposta = message.recv(2048)

        responder = resposta.decode("utf-8").upper()

        r.sendto(responder.encode("utf-8"), ("Labin-PC", 3127))

except Exception as erro:
    print(erro)
    r.close()
