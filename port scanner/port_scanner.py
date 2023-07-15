import sys
import socket
import time
begin= time.time()
if len(sys.argv)<=1:
	print(f"usage: {sys.argv[0]} ip start(optional) end(optional) ")
	exit(1)


ip= sys.argv[1]
start=1
end=65535

#user din't give input
if len(sys.argv) >= 3:
	start=int(sys.argv[2])
if len(sys.argv)>=4:
	end=int(sys.argv[3])

def check_port_status(port=int):
	try:
		s=socket.socket()
		s.settimeout(0.001)
		s.connect((ip,port))
		return True
	except(ConnectionRefusedError, socket.timeout,PermissionError):
		return False

for port in range(start,end):

	response = check_port_status(port)
	if response:
		  print(f"Open Port Found [{port}]")


end = time.time()
print(f"time taken-->{end-begin}")