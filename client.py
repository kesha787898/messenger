import socket
import threading
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 53210))


def inn():
    print("inn")
    while True:
        a=input()
        if a=="ex":
            client_sock.close()
            break
        client_sock.sendall(bytes(a,'utf-8'))
        
def out():
    print("out")
    while True:
        data = client_sock.recv(1024)
        if data:
            print(data)

a=threading.Thread(target=inn)
b=threading.Thread(target=out)
#a.daemon=True
#b.daemon=True
a.start()
b.start()
