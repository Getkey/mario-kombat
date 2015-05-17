from client import clib
from engine import character
from client import serialize

mario = character.Character(10, 20)
pseudo = input("What's your name?")
characters = {pseudo: mario}

ip = "localhost"#input("Server's IP: ")
port = 9876#int(input("Server's port: "))

clib = clib.Clib(ip, port)
clib.sendMessage(serialize.gen_handshake_msg(pseudo))# TODO: Send this reliably
print(mario)

a = 0
while True:
	clib.pool(characters, mario)
	a += 1
	if a == 100000:
		a = 0
		clib.sendMessage(serialize.gen_input_msg(21))
		print("le", mario.x)
