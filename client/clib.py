#!/usr/bin/python3
import socket
import protobuf3

class Clib(object):
	def __init__(self, proto_file, srv_ip, srv_port):
		self.meta = {}
		#create an object in meta for every possible message

		self.usr_prot = __import__(proto_file)
		self.srv_data = (srv_ip, srv_port)

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.setblocking(False)

	def pool(self):
		#pools
		self.sock.bind(self.srv_data)
		
		try:
			self.sock.recv(1024)
			#deserialize
			#self.meta = #what's has been deserialized
		except BlockingIOError:
			return

	def getMessage(self, msg_name):
		return self.meta[msg_name]

	def sendMessage(self, message):
		self.sock.sendto(message, self.srv_data)

a = Clib('sys', '127.0.0.1', 9876)

b = a.pool()
print(b)
