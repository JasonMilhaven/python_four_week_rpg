

from Transform import *

TILE_SCALE = 32

class Tile(Transform):
	
	def __init__(self, posX = 0, posY = 0, sizeX = TILE_SCALE, sizeY = TILE_SCALE):
		super().__init__(posX, posY, sizeX, sizeY)
				
		self.img = None
	
	
	def set_size_x(self, x):
		__x__ = TILE_SCALE
	
	def set_size_y(self, y):
		__Y__ = TILE_SCALE