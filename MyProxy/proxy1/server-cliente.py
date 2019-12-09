import socket
from threading import Thread
def client(h, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4,tipo de socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while True:
        try:
            s.connect((h, port))
            break
        except Exception as e:
            pass

    print("Conectou")
    msg = ("")
    while msg != ("Fim"):
        msg = input("Entre com a mensagem: ")
        s.sendto(msg)# Envia dados
        var = s.recv(1024)
        print(var)
    s.close()  # Termina conexao
    print("Fechou a conexao")
if __name__ == '__main__':
    w = input("IP:")
    port2= input("PORT:")
client(w,port2)
