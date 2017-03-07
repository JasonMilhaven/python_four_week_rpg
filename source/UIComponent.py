import pygame

from Transform import *
from utilities import *

# extend from this class and override the methods
# or set the callback functions upon instantiation, either works ok

class UIComponent(Transform):

	def __init__(self, posX = 0, posY = 0, sizeX = 0, sizeY = 0):
		super().__init__(posX, posY, sizeX, sizeY)
		
		self.__visible__ = True
		self.color = GRAY
		self.borderColor = WHITE
		self.borderSize = 2
		
		self.set_visible_func = None
		self.onclicked_func = None
		self.on_hover_begin_func = None
		self.on_hover_end_func = None
		
		
	def get_visible(self):
		return self.__visible__
	
	def set_visible(self, v):
		self.__visible__ = v
		if self.set_visible_func:
			self.set_visible_func()
	
	def on_clicked(self):
		if self.on_clicked_func:
			self.on_clicked_func()
		
	def on_hover_begin(self):
		if self.on_hover_begin_func_func:
			self.on_hover_begin_func_func()
		
	def on_hover_end(self):
		if self.on_hover_end_func_func:
			self.on_hover_end_func_func()

