

from Entity import *

"""
	******************************************************************************

	Class: Player
	
	Description: Represents the player Entity in a game.
	
	Author: Jason Milhaven
	
	History:
	
	******************************************************************************
"""

class Player(Entity):

	def __init__(self, posX = TILE_SCALE * 0.5, posY = TILE_SCALE * 0.5, room):
		super().__init__(posX, posY, room)
		
		