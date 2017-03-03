from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler


class Server(ThreadingMixIn, TCPServer):pass
class Handler(StreamRequestHandler):

	def handle(self):
		addr=self.request.getpeername()
		print 'Got connection from', addr
		self.wfile.write('Thank you for connecting')
	
server=TCPServer(('',1024),Handler)
server.serve_forever()