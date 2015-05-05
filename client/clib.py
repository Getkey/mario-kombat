#!/usr/bin/python3
import socket
from client import deserialize

class Clib(object):
	def __init__(self, proto_file, srv_ip, srv_port):
		self.meta = {}
		#create an object in meta for every possible message
		self.meta.chat = []
		# Or use them directly in the game engine?

		self.usr_prot = __import__(proto_file)
		self.srv_data = (srv_ip, srv_port)

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.setblocking(False)

	def pool(self):
		#pools
		self.sock.bind(self.srv_data)
		
		try:
			byte_msg = self.sock.recv(1024)
			#self.meta = refresh(byte_msg, self.meta)
			#deserialize
			#self.meta = #what's has been deserialized
		except BlockingIOError:
			return

	def getMessage(self, msg_name):
		return self.meta[msg_name]

	def sendMessage(self, message):
		self.sock.sendto(message, self.srv_data)

	def getChat(self):
		chat = self.meta.chat

a = Clib('sys', '127.0.0.1', 9876)

b = a.pool()
print(b)
