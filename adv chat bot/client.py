#!/usr/bin/python

import socket
import threading

def send_msg():
	while True:
		print("Nick-->",end="")
		s.send(input().encode())

def recv_msg():
	while True:
		msg=s.recv(1024).decode()
		print(f"Tom--> {msg}")
		if msg == "exit":
			s.close()


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
	try:
		s.connect(("127.0.0.1",9999))
		break
	except ConnectionRefusedError:
		pass


t1=threading.Thread(target=send_msg)
t1.start()
recv_msg()

