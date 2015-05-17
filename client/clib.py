#!/usr/bin/python3
import socket
from client import deserialize

class Clib(object):
	def __init__(self, srv_ip, srv_port):
		self.srv_data = (srv_ip, srv_port)

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.setblocking(False)
		self.sock.connect(self.srv_data)

	def pool(self, characters, me):
		try:
			byte_msg = self.sock.recv(1024)
			deserialize.refresh(byte_msg, characters, me)
		except BlockingIOError:
			return

	def sendMessage(self, message):
		self.sock.send(message)
