from protocol import server_to_client as s2c

def add_ack(client, instance, reliable):
	# We should do
	# instance.ack = 15
	# instance.ack = 100
	# But there's a bug in protobuf3 (cf readme.md)
	p_ack = instance.Ack()
	p_ack.ack, p_ack.ackfield = client.remote_seq.compose_ack()
	instance.ack = p_ack

	if reliable:
		instance.reliable = client.local_seq.get_id()

	return instance.encode_to_bytes()

def mk_position_message(clients):
	instance = s2c.Datagram()
	instance.type = instance.Type.POSITION

	for cl in clients:
		if cl.ready:
			p_cl = instance.position.Character()
			p_cl.nickname = cl.nickname
			p_cl.x = cl.character.x
			p_cl.y = cl.character.y

			instance.position.character.append(p_cl)

	return instance

def mk_chat_message(clients):
	instance = s2c.Datagram()
	instance.type = instance.Type.CHAT

	for cl in clients:
		p_cl = instance.chat.Character()
		p_cl.nickname = "Jean-Pierre"# Messages will be buffered
		p_cl.msg = "Salut."# These are only placeholders

		instance.chat.character.append(p_cl)

	return instance
