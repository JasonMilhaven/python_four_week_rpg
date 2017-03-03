

from Transform import *

class Tile(Transform):
	
	def __init__(self, posX = 0, posY = 0, sizeX = 0, sizeY = 0):
		super().__init__(posX, posY, sizeX, sizeY)
		
		self.TILE_SET_MODIFIER = 20
		
		self.img = None