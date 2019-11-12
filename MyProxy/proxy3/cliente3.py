import socket
import threading 
import time

tLock = threading.Lock() 
shutdown = False

def receiving(name, sock):
    while not shutdown: 
        try:
            tLock.acquire()
            while True:
                data, addr = s.recvfrom(1024)   
                data = data.decode('utf-8')
                print(str(data))
            print("Cliente Conectado em: " + addr)
        except:
            pass

        finally:
            tLock.release()

host = "0.0.0.0"
port = 3128

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rt = threading.Thread(target=receiving, args=("RecvThread", s))
rt.start()

name = input("Enter your name: ")
message = input("> ")
while message != "q":
    if message != '':
        print("From ",name)
        s.sendto('{}: {}'.format(name, message).encode('utf-8'), (host,port))
        

    tLock.acquire()
    message = input('')
    tLock.release()
    time.sleep(0.5)

shutdown = True
rt.join()
s.close()