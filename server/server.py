#!/usr/bin/python3
import asyncio
from server import player
from server import deserialize
from server import serialize

class GameServerProtocol(asyncio.DatagramProtocol):# UDP
	
	def __init__(self):
		self.clients = []

	def connection_made(self, transport):
		print(transport)# Dunno if this is gonna be usefull

	def connection_lost(self, exc):
		print("Connection lost: ", exc)

	def datagram_received(self, data, addr):
		cl_ip, cl_port = addr

		def already_here():# Do that in the player Class
			for i in self.clients:
				if i.ip == cl_ip and i.port == cl_port:
					return i
			raise LookupError('Not already here')# New client

		print('We got ' + data.decode())

		# We set a callback that gets trigered if the client hasn't acked in the last 10 secondes
		try:
			client = already_here()
			client.handle.cancel()
			client.handle = loop.call_later(10, self.clients.remove, client)
		except LookupError:
			client = player.Player(cl_ip, cl_port)
			self.clients.append(client)

			client.handle = loop.call_later(10, self.clients.remove, client)

		deserialize.route_data(data, client.remote_seq, client)


def broadcast(delay):# Periodically tells players what the game state is
	start_time = loop.time()
	print("broadcast", transport, protocol.clients)

	encoded_to_be_sent = serialize.mk_position_message(protocol.clients)
	print(encoded_to_be_sent)

	for cl in protocol.clients:
		transport.sendto(encoded_to_be_sent, (cl.ip, cl.port))

	loop.call_at(start_time + delay, broadcast, delay)# Note: if scheduled to time in the past; runs NOW!


loop = asyncio.get_event_loop()

listen = loop.create_datagram_endpoint(GameServerProtocol, ('127.0.0.1', 9876))
transport, protocol = loop.run_until_complete(listen)

broadcast(1)# delay in seconds

try:
	loop.run_forever()
except KeyboardInterrupt:# Exit on ^C
	pass# Harsly closes the server
