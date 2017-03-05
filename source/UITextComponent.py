
from UIComponent import *

class UITextComponent(UIComponent):
	
	def __init__(self, posX = 0, posY = 0, sizeX = 0, sizeY = 0):
		super().__init__(posX, posY, sizeX, sizeY)
		
		self.font = load_font("Zig.ttf", 16)
		self.text = ""
		
	def draw(self, screen):
		super().draw(screen)
	
		if self.text != "" and self.font != None:
			screen.blit(
				self.font.render(self.text, 1, WHITE),
				(self.get_pos_x() - self.get_size_x() * 0.25, self.get_pos_y() - self.get_size_y() * 0.25)
			)