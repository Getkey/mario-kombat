from protocol import client_to_server as c2s
from engine import engine
from server import player


def use_chat(msg):#this should be in the game engine
	print("The chat message contains: ", msg)

def route_data(b_string, remote_seq, player):
	message = c2s.Datagram()
	try:
		message.parse_from_bytes(b_string)
		if message.reliable:
			print(message.reliable, remote_seq.compose_ack())
			# update our ackstack so that the next time
			# a packet is sent the client is notified
			remote_seq.update_bitfield(message.reliable)
			print(remote_seq.compose_ack())
		if player.ready:
			if message.type is message.Type.INPUT:
				print("This is an input")
				engine.use_input(player, message.input.key)
			elif message.type is message.Type.CHAT:
				engine.use_chat(player, message.chat.msg)
				print("This is a chat message")
			else:
				print("None of the above. WTF")
		elif message.type is message.Type.HANDSHAKE:
			print("This is a handshake")
			player.set_nickname(message.handshake.nickname)
		else:
			print("Don't you know it's impolite to talk to people before greeting them?\nHint: shake my hand.")

	except ValueError:
		print("What is this garbage? Disregard it.")


# Test
#from protocol import reliability
#remote_seq = reliability.remote_seq

#route_data(b"\x08\x02\x12\x04\x08\x1e\x10d*?\n\x15\n\x0bJean-Pierre\x12\x06Salut.\n&\n\x06P\xc3\xa9p\xc3\xa9\x12\x1cMregn\xc3\xa9 d'mon temps...mrbmmr", remote_seq)
