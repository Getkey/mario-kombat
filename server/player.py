#!/usr/bin/python3
from engine import character
from protocol import reliability

class Player(object):
	def __init__(self, ip, port):
		self.ready = False

		self.ip = ip
		self.port = port
		self.remote_seq = reliability.Remote_seq()
		self.local_seq = reliability.Local_seq()

		self.character = character.Character(30, 348)

	def set_nickname(self, nickname):# Get player ready
		self.nickname = nickname
		self.ready = True

players = []

a = Player(4356, 7657)
