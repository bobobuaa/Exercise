import socket

s=socket.socket()

host=socket.gethostname()
port=1024
s.bind((host,port))

s.listen(5)
while True:
	c, addr=s.accept()
	print 'Got connection from', addr
	c.send('Thank you for connecting')
	c.send('Success')
	
	c.recv(1024)
	c.close()