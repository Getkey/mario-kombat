# THIS IS DOCUMENTATION
# See clib_doc.md
# To be included in the client.
from protocol import client_to_server as c2s

def gen_ack_msg():
	ack_msg = c2s.Ack()

	ack_msg.ack = 12
	ack_msg.ackfield = b"fji56"
	
	return ack_msg


def gen_chat_msg(msg):
	instance = c2s.Datagram()# This 
	instance.type = instance.Type.CHAT

	instance.chat.msg = msg
	
	instance.ack = gen_ack_msg()# And this are redundant

	return instance.encode_to_bytes()

def gen_input_msg(key):
	instance = c2s.Datagram()
	instance.type = instance.Type.INPUT

	instance.input.key = key

	instance.ack = gen_ack_msg()

	return instance.encode_to_bytes()

def gen_handshake_msg(nickname):
	instance = c2s.Datagram()
	instance.type = instance.Type.HANDSHAKE

	instance.handshake.nickname = nickname

	instance.ack = gen_ack_msg()

	return instance.encode_to_bytes()
