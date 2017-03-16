
import random

from Tile import *
from utilities import *
from Monster import *

"""
	******************************************************************************

	Class: Room
	
	Description: Container for tiles, entities, and borderingRooms.  Represents a place
	that the player will walk around.  Will get serialized alongside the Game instances.
	
	Author: Jason Milhaven
	
	History:
	
	******************************************************************************
"""

class Room():

	"""
		==============================================================================
		
		Method: __init__
		
		Description: Constructor for Room class, creates fields for rooms, tiles, and
		entities.  Creates a room.
		
		Author: Jason Milhaven
		
		History:
		
		==============================================================================
	"""

	def __init__(self, width, height, player):
		
		self.player = player
		self.tiles = []
		self.entities = []
		self.borderRooms = []
		
		self.entities.append(player)
		
		self._create_room_(width, height)
		

	def _create_room_(self, width, height):
		for x in range(0, width, TILE_SCALE):
			for y in range(0, height - 4 * TILE_SCALE, TILE_SCALE):
				t = Tile(x + TILE_SCALE * 0.5, y + TILE_SCALE * 0.5, TILE_SCALE, TILE_SCALE)
				if random.randint(0, 3) == 0:
					t.img = load_img("GrassMts.png")
					t.isBlocking = True
				self.tiles.append(t)
		for i in range(0, 4):
			print("")
			Monster(10, 10)

			
			