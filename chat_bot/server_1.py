
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("127.0.0.1",1111))
s.listen(1)

client,addr =s.accept()
#client.send(b"hello")

while True:
	cmd=input("$ ")
	client.send(cmd.encode())
	output=(client.recv(1024)).decode()
	print(output)