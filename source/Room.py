

from Tile import *
from utilities import *

class Room():

	def __init__(self, width, height, player):
		self.tiles = []
		self.entities = []
		self.borderRooms = []
		
		self.entities.append(player)
		
		self._create_room_(width, height)
		

	def _create_room_(self, width, height):
		for x in range(0, width, TILE_SCALE):
			for y in range(0, height - 4 * TILE_SCALE, TILE_SCALE):
				t = Tile(x + TILE_SCALE * 0.5, y + TILE_SCALE * 0.5, TILE_SCALE, TILE_SCALE)
				t.img = load_img("TestTile.png")
				self.tiles.append(t)