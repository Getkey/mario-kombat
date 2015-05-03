# THIS IS DOCUMENTATION
# See clib_doc.md
# To be included in the client.
from protocol import client_to_server as c2s

instance = c2s.Datagram()
instance.type = instance.Type.CHAT

instance.chat.msg = "Salut."
# Send message
print(instance.encode_to_bytes())
