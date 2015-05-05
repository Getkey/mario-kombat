from protocol import client_to_server as c2s


def use_chat(msg):#this should be in the game engine
	print("The chat message contains: ", msg)

def route_data(b_string, remote_seq):
	message = c2s.Datagram()
	try:
		message.parse_from_bytes(b_string)
		if message.reliable:
			print(message.reliable, remote_seq.compose_ack())
			# update our ackstack so that the next time
			# a packet is sent the client is notified
			remote_seq.update_bitfield(message.reliable)
			print(remote_seq.compose_ack())

		if message.type is message.Type.INPUT:
			print("This is an input")
			#use_input(message.input.x)
		elif message.type is message.Type.CHAT:
			print("This is a chat message")
			use_chat(message.chat.msg)
		elif message.type is message.Type.HANDSHAKE:
			print("This is an handshake")
			#use_handshake(message.handshake.nickname)
		else:
			print("None of the above. WTF")

	except ValueError:
		print("What is this garbage? Disregard it.")


# Test
#from protocol import remote_sequence
#remote_seq = remote_sequence.remote_seq

#route_data(b"\x08\x02\x12\x04\x08\x1e\x10d*?\n\x15\n\x0bJean-Pierre\x12\x06Salut.\n&\n\x06P\xc3\xa9p\xc3\xa9\x12\x1cMregn\xc3\xa9 d'mon temps...mrbmmr", remote_seq)
