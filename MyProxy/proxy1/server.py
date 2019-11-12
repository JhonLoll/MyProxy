import socket
from threading import Thread
L=[]

def ConversaSimultanea(a,b):
    mensagem = ""
    while mensagem != "Fim":
        print("entrou no loop da conversa")
        mensagem = L[a].recv(5000)
        if not mensagem:
            break
        L[b].sendall(mensagem)
    conn.close()

#h = raw_input("Entre com o IP do Servidor local: ")
#port = input("Entre com a Porta do Servidor local: ")

h = ("0.0.0.0")
port = 3128

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4,tipo de socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Ta Quase POURAA")
server.bind((h, port))  # liga o socket com IP e porta
server.listen(5)  # espera chegar pacotes na porta especificada
print("Waiting")

for i in range(2):
    print("Waiting the First IP")
    conn, addr = server.accept()  # as variaveis conn a addr sao preenchidas pela funcao accept
    L.append(conn)
    print("AEE POURRA")
t1 = Thread(target=ConversaSimultanea, args=(1,0,)).start()
t2 = Thread(target=ConversaSimultanea, args=(0,1,)).start()
