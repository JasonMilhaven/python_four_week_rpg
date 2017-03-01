import pygame

from Transform import *
from utilities import *

# extend from this class and override the methods

class UIComponent(Transform):

	def __init__(self, posX = 0, posY = 0, sizeX = 0, sizeY = 0):
		super().__init__(posX, posY, sizeX, sizeY)
		
		self.__visible__ = False
		self.color = RED
		self.borderColor = BLUE
		self.borderSize = 2
	
	def get_visible(self):
		return self.__visible__
	
	def set_visible(self, v):
		self.__visible__ = v
		
	def on_clicked(self):
		pass
		
	def on_hover_begin(self):
		pass
	
	def on_hover_end(self):
		pass
