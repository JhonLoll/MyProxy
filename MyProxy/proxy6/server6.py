import socket
import time

host = 3127

bridge = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bridge.connect(("10.1.2.104", 3125))

try:
    bridge.bind(("0.0.0.0", host))

    bridge.listen(5)

    print("Ponte iniciada em %s %s" %("0.0.0.0", host))

    (data, cliente) = bridge.accept()

    cliente[0]

    print("Conectado por: %s" %cliente[0])

    while True:

        message = data.recv(2048)

        msgs = message.decode('utf-8').upper()

        # bridge.sendto(msgs.encode("utf-8"),("localhost", 3128))

        print(str(msgs.decode('utf-8')))

except Exception as erro:
    print(erro)
    bridge.close()