import socket

def client(h, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while True:
        try:
            s.connect((h, port))
            break
        except Exception as e:
            pass

    print("Conectou")
    msg = ""
    while msg != "Fim":
        msg = input("Entre com a mensagem: ")
        s.send(msg.encode())  # Codifica a mensagem antes de enviar
        var = s.recv(1024).decode()  # Decodifica a mensagem recebida
        print(var)
    s.close()
    print("Fechou a conexão")

if __name__ == '__main__':
    w = input("IP: ")
    port2 = int(input("PORT: "))  # Certifique-se de que a porta é um número inteiro
    client(w, port2)