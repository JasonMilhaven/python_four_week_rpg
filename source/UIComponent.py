import pygame

from Transform import *
from utilities import *

class UIComponent(Transform):

	def __init__(self, posX = 0, posY = 0, sizeX = 0, sizeY = 0):
		super().__init__(posX, posY, sizeX, sizeY)
		
		self.__visible__ = False
		self.color = RED
		self.borderColor = BLUE
		self.borderSize = 2
		self.onClicked = None
	
	def get_visible(self):
		return self.__visible__
	
	def set_visible(self, v):
		self.__visible__ = v
		
	def on_clicked(self):
		if self.onClicked:
			self.onClicked()