#!/user/bin/python
print ('''created and developed by tor bhai studio. visit us on our site to learn hacking , programming, web developement and many more for free.
https://torbhai.in ''')
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input ("input victims target  ip  ")
port = input ("input the port  ")
def torscanner(port):
	     if sock.connect_ex({host,port}):
		           print "the %d port is closed" % (port)
	     else:
		           print "the %d port is open" % (port)
torscanner(port)
