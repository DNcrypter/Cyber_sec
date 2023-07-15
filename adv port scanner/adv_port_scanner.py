from argparse import ArgumentParser
from socket import socket
from threading import Thread
from time import time

open_ports=[]

#creating help menu:
def prepare_args():
	parser= ArgumentParser(description="it is adv port scanner",usage="%(prog)s 192.168.1.2",epilog="Example - %(prog)s -s 20 -e 4000 -t 20 -V ")
	parser.add_argument(metavar="IPv4",dest="ip",help="host to scan")
	#-> optional arguments:
	parser.add_argument("-s","--start",dest="start",metavar="\b",type=int,help="....starting port",default=1)
	parser.add_argument("-e","--end",dest="end",metavar="\b",type=int,help="....ending port",default=65535)
	parser.add_argument("-t","--thread",dest="thread",metavar="\b",type=int,help="....thread to use",default=30)
	parser.add_argument("-V","--verbose",dest="verbose",action="store_true",help="verbose output")
	parser.add_argument("-v","--version",action="version",version="%(prog)s 1.0")
	arg=parser.parse_args()
	return arg

	#to remove "space" caused by metavar in help menu--->use \b

	"""dest=,type=,help=,metavar=,default=,--start,--end,--thread,--verbose,--version"""
def prepare_ports(start:int,end:int):
	""" generator function for ports

		arguments-->
		   start(int) - starting port
		   end(int)   - ending port
	"""
	for port in range(start,end+1):
		yield port                   
"""# yield -> store in memory similar to array but 
remove element after one use
# inshort, store all ports in yield and return
its location where fuction will be called."""

def scan_port():
	"""scan ports
	"""
	while True:
		try: 
			s=socket.socket()
			s.settimeout(1)
			port=next(ports)
			s.connect((argument.ip,port))
			open_ports.append(port)
			if argument.verbose:
				print(f"{open_ports}",end="")  

									    	#as it get open port it print list every time.
				 					    	# to print new list inplace of previous we use.
				 					    	# \r remove all that line and print newline.
				 					    	# overwrite the content.

		except (ConnectionRefusedError,socket.timeout):
			continue
		except StopIteration:
			break

def prepare_threads(threads:int):
	"""create,start,join threads

		arguments:
	   		threads(int) -- number of threads to use
	"""
	thread_list=[]
	for _ in range(threads+1):		 # we use _ here because we don't have to print it.					
		thread_list.append(Thread(target=scan_port))
	for thread in thread_list:
		thread.start()
	for thread in thread_list:
		thread.join()				#join() -> simplly tells that, don't exit till main
									#  			 thread complete.
	                           		#main thread -->it is thread that starts all threads.




if __name__=="__main__":
	arguments=prepare_args()
	ports=prepare_ports(arguments.start,arguments.end)
	start_time=time()
	thread=prepare_threads(arguments.thread)
	end_time=time()
	print(f"open port found [{open_ports}]")
	print(f"total time taken {round(end_time-start_time)}")

