# IMHO this should be in the game engine
# to directly modify the players' values
from protocol import server_to_client as s2c

def refresh(byte_msg, meta_obj):
	message = s2c.Datagram()

	try:
		message.parse_from_bytes(byte_msg)
#		if message.type is message.Type.INPUT:
#			do_game_engine_stuff()
		#el
		if message.type is message.Type.HEALTH:
			# Maybe I could directly put that in the characters... Meh...
		elif message.type is message.Type.CHAT:
			for i in message.chat.character:
				chat_data = {"character": #get char from name, "data": message.chat
				meta_obj.append(chat_data)
		elif message.type is message.Type.GAMEOVER:

