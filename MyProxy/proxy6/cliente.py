import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("localhost", 3127))

while True:

    data = input("Digite a mensagem: ")
    cliente.sendto(data.encode('utf-8'), ("localhost", 3127))

    (responder, bridge) = cliente.recvfrom(2048) 

    print(responder.decode('utf-8'))


