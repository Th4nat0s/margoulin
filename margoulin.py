#!/usr/bin/python

from sys import argv
import shlex
from subprocess import call


#http://www.ebnj.net/pythongzipbenchmarks
def gziplines(fname):
	from subprocess import Popen, PIPE
	f = Popen(['zcat',fname],stdout = PIPE)
	for line in f.stdout:
		yield line

for line in gziplines(argv[1]):
#os.popen("zcat"+argv[1])
#file_path=sys.argv[1]
#log_fh=open(file_path,'r')
#for line in log_fh.readlines():
	log_line=shlex.split(line)
	path=log_line[6].split(" ",2)	
	http_request="http://"+log_line[0]+path[1]
	http_status=log_line[7]
	if int(http_status) == (200 or 301 or 302 or 304):
		if (('?' in http_request) and ('=' in http_request)):
			print http_status,http_request+"\n"

