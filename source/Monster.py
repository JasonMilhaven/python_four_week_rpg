

from Entity import *

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
	
	def __init__(self, posX = 0, posY = 0):
		super().__init__(posX, posY)
		
	__offsets__ = []	
	__offsetStartingPoint__ = self.get_pos()
	__currentOffset__ = 0
	
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
		
		# and call attack method