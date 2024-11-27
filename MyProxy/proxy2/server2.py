import socket
from threading import Thread

L = []

def ConversaSimultanea(client_socket, client_index):
    while True:
        try:
            mensagem = client_socket.recv(5000).decode()  # Decodifica a mensagem recebida
            if not mensagem or mensagem == "Fim":
                break
            
            # Envia a mensagem para todos os outros clientes
            for i, conn in enumerate(L):
                if i != client_index:  # Não envia para o próprio cliente
                    conn.sendall(mensagem.encode())  # Codifica a mensagem antes de enviar
        except Exception as e:
            print(f"Erro na conexão do cliente {client_index}: {e}")
            break

    client_socket.close()  # Fecha a conexão após a conversa
    L.remove(client_socket)  # Remove o cliente da lista

h = "0.0.0.0"
port = 3128

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Servidor iniciado...")
server.bind((h, port))
server.listen(5)

while True:
    print("Aguardando novos clientes...")
    conn, addr = server.accept()
    L.append(conn)
    print(f"Cliente conectado: {addr}")

    # Inicia uma nova thread para cada cliente
    client_index = len(L) - 1
    Thread(target=ConversaSimultanea, args=(conn, client_index)).start()