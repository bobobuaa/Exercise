import socket
s=socket.socket()
 
host='GK-N-WANGHAIBO'
port=1024
 
s.connect((host,port))
print s.recv(1024)
print s.recv(1024)

print s.send("Test send")