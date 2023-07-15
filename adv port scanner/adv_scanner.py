from argparse import ArgumentParser
import socket
from threading import Thread
from time import time

open_ports=[]



def prepare_args():

	parser=ArgumentParser(description="This is adv Port scanner",usage="%(prog)s 192.168.1.2 ",epilog="example: %(prog)s 192.168.1.2 -s 1 -e 400 -t 20 -V -v ")
#positional args:
	parser.add_argument(metavar="IPv4",dest="ip",help="required IP")
#optional args:
	parser.add_argument("-s","--start",metavar="\b",dest="start",type=int,help="....starting port",default=1)
	parser.add_argument("-e","--end",metavar="\b",dest="end",type=int,help="....ending port",default=65535)
	parser.add_argument("-t","--thread",metavar="\b",dest="thread",type=int,help="....number of threads",default=200)
	parser.add_argument("-V","--verbose",dest="verbose",action="store_true",help="verbose output")
	parser.add_argument("-v","--version",dest="version",action="version",version="%(prog)s 1.0")

	args=parser.parse_args()
	return args

def prepare_ports(start:int,end:int):
	"""preparing ports   - generator function

		arguments:
			start(int) - starting port
			end(int)   - ending port
	 """

	for port in range(start,end+1):
	 yield port


def scan_ports():
	while True:
		try:
			s=socket.socket()
			s.settimeout(1)
			port=next(ports)
			s.connect((arguments.ip,port))
			open_ports.append(port)
			if arguments.verbose:
				print(f"\rfinding open ports {open_ports}",end="")

		except (ConnectionRefusedError,socket.timeout,PermissionError):
			continue
		except StopIteration:
			break
def prepare_threads(thread:int):
	#used threadlist to store all threads

	thread_list=[]

	for _ in range(thread+1):
		thread_list.append(Thread(target=scan_ports))
	for thread in thread_list:
		thread.start()
	for thread in thread_list:
		thread.join()



def total_time():

	print(f"total time taken {round(end_time-start_time,3)}")

if __name__=="__main__":

	start_time=time()

	logo=open("logo.txt","r")
	print(f"{logo.read()}")
	logo.close()

	arguments=prepare_args()
	ports=prepare_ports(arguments.start,arguments.end)
	prepare_threads(arguments.thread)
	
	if arguments.verbose:
		print()

	print(f"open port found {open_ports}")


	end_time=time()

	total_time()



