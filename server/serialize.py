# THIS IS DOCUMENTATION!
# To be included in the server.
from protocol import server_to_client as s2c

instance = s2c.Datagram()
instance.type = instance.Type.CHAT

# instance.reliable = 12

# We should do
# instance.ack = 15
# instance.ack = 100
# But there's a bug in protobuf3 (cf readme.md)
lul = instance.Ack()
lul.ack = 15
lul.ackfield = 100
instance.ack = lul

lel = instance.chat.Character()
lel.nickname = "Jean-Pierre"
lel.msg = "Salut."

lol = instance.chat.Character()
lol.nickname = "Pépé"
lol.msg = "Mregné d'mon temps...mrbmmr"

instance.chat.character.append(lel)
instance.chat.character.append(lol)
# Send message
print(instance.encode_to_bytes())
