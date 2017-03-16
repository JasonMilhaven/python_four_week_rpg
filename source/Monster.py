

from Entity import *
from utilities import*
"""
	******************************************************************************

	Class: Monster
	
	Description: Represents a monster Entity in a game.  Monsters will move in a
	set of offsets until a player is found.
	
	Author: Jason Milhaven
	
	History:
	
	******************************************************************************
"""

class Monster(Entity):
	
	def __init__(self, posX = 0, posY = 0, room):
		super().__init__(posX, posY, room)
		
		self.__sightRadius__=5
		self.__offsets__ = []	
		self.__offsetStartingPoint__ = self.get_pos()
		self.__currentOffset__ = 0
		
	def next_offset(self):
		if self.__currentOffset__ >= len(self.__offsets__) - 1
			self.__currentOffset__ = 0
		else:
			self.__currentOffset__ += 1
	
	def update(self, frameDelta):
		super().update(frameDelta)
		
		if self.get_pos_x() >= self.offsetStartingPoint[0] + offsets[self.__currentOffset__][0] and self.get_pos_y() >= self.offsetStartingPoint[1] + offsets[self.__currentOffset__][1]:
			self.next_offset()
		
		if self.get_move_x() == 0 and self.get_move_y() == 0:
			next_offset()
		
		# finish the player sight
		if distance(self,self._room_.player) <=self.__sightRadius__:
			self.set_move_x(clamp01(player.get_pos_x() - self.get_pos_x()))
			self.set_move_y(clamp01(player.get_pos_y() - self.get_pos_y()))
		# and call attack method
		
		if distance(self,self._room_.player) <= self.range:
			self.attack(self._room_.player)
		
		