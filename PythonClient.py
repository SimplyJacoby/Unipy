import os
import threading
from socket import *

def mainServer():
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        sock.connect(("54.92.132.97", 7734))
        # Local 10.20.0.10
        # VM Ubuntu Server 127.0.0.1
        # AWS Ubuntu server 54.92.132.97 **Not static so will change**
    except:
        print("Could not connect to server")
        os._exit(1)
    sock.send(bytes(("hello from client\n").encode()))
    print(str(sock.recv(4096).decode()))
    sock.close()
    os._exit(1)
    
def main():
    mainServer()

if __name__ == "__main__":
    main()