#!/usr/bin/python3
import asyncio
from client import serialize

import socket

ip = "127.0.0.1"
port = 9876

msg1 = serialize.gen_handshake_msg("Pépé")
msg2 = serialize.gen_chat_msg("Mrégnégné d'mon temps")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(msg1, (ip, port))
sock.sendto(msg2, (ip, port))
