import socket
from threading import Thread

L = []

def ConversaSimultanea(a, b):
    mensagem = ""
    while mensagem != "Fim":
        print("entrou no loop da conversa")
        mensagem = L[a].recv(5000).decode()  # Decodifica a mensagem recebida
        if not mensagem:
            break
        L[b].sendall(mensagem.encode())  # Codifica a mensagem antes de enviar
    L[a].close()  # Fecha a conexão após a conversa

h = "10.113.50.208"
port = 3128

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Ta Quase POURAA")
server.bind((h, port))
server.listen(5)
print("Waiting")

for i in range(2):
    print("Waiting for the First IP")
    conn, addr = server.accept()
    L.append(conn)
    print("AEE POURRA")

t1 = Thread(target=ConversaSimultanea, args=(1, 0)).start()
t2 = Thread(target=ConversaSimultanea, args=(0, 1)).start()