#!/usr/bin/python3
import asyncio
import time

import socket

ip = "127.0.0.1"
port = 9876
msg = b"Plop"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
	time.sleep(2)
	sock.sendto(msg, (ip, port))
	print("Sent")
