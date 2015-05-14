# THIS IS DOCUMENTATION!
# To be included in the server.
from protocol import server_to_client as s2c

instance = s2c.Datagram()
instance.type = instance.Type.CHAT

def mk_ack_message():
	# We should do
	# instance.ack = 15
	# instance.ack = 100
	# But there's a bug in protobuf3 (cf readme.md)
	p_ack = instance.Ack()# TODO: use real values
	p_ack.ack = 15
	p_ack.ackfield = 100
	instance.ack = p_ack


def mk_position_message(clients):
	mk_ack_message()

	for cl in clients:
		if cl.ready:
			p_cl = instance.position.Character()
			p_cl.nickname = cl.nickname
			p_cl.x = cl.character.x
			p_cl.y = cl.character.y

			instance.position.character.append(p_cl)

	return instance.encode_to_bytes()

def mk_chat_message(clients):
	mk_ack_message()

	instance.reliable = 12

	for cl in clients:
		p_cl = instance.chat.Character()
		p_cl.nickname = "Jean-Pierre"# Messages will be buffered
		p_cl.msg = "Salut."# These are only placeholders

		instance.chat.character.append(p_cl)

	return instance.encode_to_bytes()
