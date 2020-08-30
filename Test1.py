#!/user/bin/python
print ('''created and developed by tor bhai studio. visit us on our site to learn hacking , programming, web developement and many more for free.
https://torbhai.in ''')
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = raw_input("[*] enter the host/ip to scan: ")
port = int(raw_input("[*] enter the port to scan: "))
def portscanner(port):
	if sock.connect_ex((host,port)):
		print ('port is closed')
	else:
		print ('given ip is open on the port')
portscanner(port)		
