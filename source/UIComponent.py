import pygame

from Transform import *
from utilities import *

# extend from this class and override the methods

class UIComponent(Transform):

	def __init__(self, posX = 0, posY = 0, sizeX = 0, sizeY = 0):
		super().__init__(posX, posY, sizeX, sizeY)
		
		self.__visible__ = True
		self.color = GRAY
		self.borderColor = WHITE
		self.borderSize = 2
		
	def get_visible(self):
		return self.__visible__
	
	def set_visible(self, v):
		self.__visible__ = v
	
	def on_clicked(self):
		print(self.name + " clicked")
		pass
		
	def on_hover_begin(self):
		print(self.name + " hover begin")
		pass
	
	def on_hover_end(self):
		print(self.name + " hover end")
		pass