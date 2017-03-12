
from UIComponent import *

"""
	******************************************************************************

	Class: UIComponent
	
	Description: Derives from UIComponent, displays text given a specific font.
	
	Author: Jason Milhaven
	
	History:
	
	******************************************************************************
"""

class UITextComponent(UIComponent):
	
	"""
		==============================================================================
		
		Method: __init__
		
		Description: Constructor for UITextComponent class, calls superclass constructor.
		Loads the default font at 16px, sets text to empty.
		
		Author: Jason Milhaven
		
		History:
		
		==============================================================================
	"""
	
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