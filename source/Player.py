

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

	def __init__(self, posX = 0, posY = 0, sizeX = TILE_SCALE, sizeY = TILE_SCALE):
		super().__init__(TILE_SCALE * 0.5, TILE_SCALE * 0.5)
		