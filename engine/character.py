#!/usr/bin/python3

class Character(object):
	def __init__(self, x, y):# Hard spawn point
		self.x = x
		self.y = y
		self._x_spawn = x
		self._y_spawn = y

	def reset_position(self):
		# This should be some sort of algo that respawns
		#the character as away as possible for other players
		# Right now it only set the player to his hard spawn point
		self.x = self._x_spawn
		self.y = self._y_spawn
