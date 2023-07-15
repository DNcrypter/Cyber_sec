#!/usr/bin/python

import socket
import threading

def send_msg():
    while True:
        print("Tom-->",end="")
        client.send(input().encode())

def recv_msg():
    while True:
        recieved = client.recv(1024).decode()
        print(f"Nick--> {recieved}")
        if recieved == "exit":
            client.close()
            s.close()

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("127.0.0.1",9999))
s.listen(1)
print("listening...")
client,addr =s.accept()
print("connected")

t1=threading.Thread(target=send_msg) # mistake--> we made thread but did use
                                    #   start() to run it.
t1.start()
recv_msg()
