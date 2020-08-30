#!/user/bin/python
#hi 
  import socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  host = input("[*] enter the host/ip to scan: ")
  port = input("[*] enter the port to scan: ")
  def portscanner(port):
  	if sock.connect_ex((host,port)):
  		print ('port is closed')
  	else:
  		print ('given ip is open on the port')
  portscanner(port)
