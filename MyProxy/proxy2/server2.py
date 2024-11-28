import socket
from threading import Thread

L = []

def ConversaSimultanea(client_socket):
    while True:
        try:
            mensagem = client_socket.recv(5000).decode()  # Decodifica a mensagem recebida
            if not mensagem or mensagem == "Fim":
                break
            
            # Envia a mensagem para todos os outros clientes
            for conn in L:
                if conn != client_socket:  # Não envia para o próprio cliente
                    conn.sendall(mensagem.encode())  # Codifica a mensagem antes de enviar
        except Exception as e:
            print(f"Erro na conexão: {e}")
            break

    client_socket.close()  # Fecha a conexão após a conversa
    L.remove(client_socket)  # Remove o cliente da lista

h = "10.113.50.208"
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
    Thread(target=ConversaSimultanea, args=(conn,)).start()