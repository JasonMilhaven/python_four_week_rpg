

from Entity import *


class Player(Entity):

	def __init__(self, posX = 0, posY = 0):
		super().__init__(posX, posY)
	
	#def update(self, frameDelta):
		#super().update(frameDelta)