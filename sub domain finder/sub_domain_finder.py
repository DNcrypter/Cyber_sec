from argparse import ArgumentParser,FileType
from requests import get, exceptions
from threading import Thread
from time import time

sub_domains=[]

def prepare_args():
	""" Prepare arguments
	"""
	parser=ArgumentParser(description="Python Based Fast Sub Domain Finder",usage="%(prog)s domain.com",epilog="Example: %(prog)s google.com -w wordlist.txt -t 200 -V ")
	parser.add_argument(metavar="domain",dest="domain",help="domain name of target")
	parser.add_argument("-w","--wordlist",dest="wordlist",metavar="",type=FileType("r"), help="wordlist to bruteforce",default="wordlist.txt")
	parser.add_argument("-t","--thread",dest="thread",metavar="",type=int, help="number of threads",default=200)
	parser.add_argument("-V","--verbose",dest="verbose",action="store_true",help="print output")
	parser.add_argument("-v","--version",dest="version",action="version",version="%(prog)s 1.0",help="print current version")

	args=parser.parse_args()
	return args

def prepare_words():
	""" generator function for words
	   argument:
	   argument.wordlist
	"""
	#creating list of words
	words=arguments.wordlist.read().split()
	for word in words:
		yield word

def prepare_threads():
	thread_list=[]
	for _ in range(arguments.thread):
		thread_list.append(Thread(target=check_sub_domain))
	for thread in thread_list:
		thread.start()
	for thread in thread_list:
		thread.join()

def check_sub_domain():

	while True:
		try:
			word = next(words)
			urls = f"https://{word}.{arguments.domain}"
			request = get(urls,timeout=10)
			if request.status_code == 200:
				sub_domains.append(urls)
			if arguments.verbose:
				print(urls)
		except (exceptions.ConnectionError,exceptions.ReadTimeout):
			continue
		except StopIteration:
			break


if __name__=="__main__":
	start_time=time()
	arguments=prepare_args()
	words=prepare_words()
	prepare_threads()
	print("sub domain found \n" + "\n".join(i for i in sub_domains))
	end_time=time()
	print(f"Number of subdomains found [ {len(sub_domains)} ]")
	print(f"total time taken {round(end_time-start_time,3)}")
	#interation --> store value in i from sub_domains.
	# "".join()--> it join all i as a single string
	# here betn "" we mention how to join each i