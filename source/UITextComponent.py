

from UIComponent import *

class UITextComponent(UIComponent):
	
	def __init__(self, posX = 0, posY = 0, sizeX = 0, sizeY = 0):
		super().__init__(posX, posY, sizeX, sizeY)
		
		self.text = ""
		
	def draw(self, screen):
		print("do the text display in UITextComponent.py")