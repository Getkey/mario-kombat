#!/usr/bin/python3
import asyncio
from client import serialize

# TODO: make this into a lib

import socket

ip = "127.0.0.1"
port = 9876
msg = serialize.gen_chat_msg("Salut.")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(msg, (ip, port))
