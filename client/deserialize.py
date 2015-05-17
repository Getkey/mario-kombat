# IMHO this should be in the game engine
# to directly modify the players' values
from protocol import server_to_client as s2c
from engine import character

def refresh(byte_msg, characters, me):
	message = s2c.Datagram()

	try:
		message.parse_from_bytes(byte_msg)
		if message.type is message.Type.POSITION:
			print("Got position message")
			for i in message.position.character:
				if i.nickname in characters:
					characters[i.nickname].x = i.x
					characters[i.nickname].y = i.y
				else:
					characters[i.nickname] = character.Character(i.x, i.y)
		elif message.type is message.Type.HEALTH:
			me.health = message.health.hp
		elif message.type is message.Type.CHAT:
			print("Got chat message")
			for i in message.chat.character:
				print(i.nickname, ":", i.msg)
		elif message.type is message.Type.GAMEOVER:
			print("Game's over")
	except ValueError:
		print("Fuck where is this shithead! Someone has thrown garbage at us!")
		pass
