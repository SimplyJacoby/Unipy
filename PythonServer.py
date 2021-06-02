from socket import *
import threading
import os

def clientThread(sock):
    try:
        while True:
            print(str(sock.recv(4096).decode()))
            sock.send(bytes(("hello from server\n").encode()))
    except:
        sock.close()
        os._exit(1)

def main():
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        sock.bind(("0.0.0.0", 7734))
    except:
        print("Port cannot be accessed")
        os._exit(1)
    try:
        while True:
            sock.listen(5)
            c, addr = sock.accept()
            thread = threading.Thread(target=clientThread, args=(c,))
            thread.start()
    except:
        sock.close()
        os._exit(1)

if __name__ == "__main__":
    main()
