#!/usr/bin/python3
import asyncio

# TODO: make this into a lib

import socket

ip = "127.0.0.1"
port = 9876
msg = b"Plop"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(msg, (ip, port))
