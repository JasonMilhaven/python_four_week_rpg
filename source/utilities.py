
import os
import pygame

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (35, 34, 34, 0.5)

"""
	******************************************************************************

	Module: utilities
	
	Description: Contains "utility" functions which are part of the program, but
	do not fit anywhere.  Contains color constants for UI, which may be moved later.
	
	Author: Jason Milhaven
	
	History: 
	
	******************************************************************************
"""

"""
	==============================================================================
	
	Method: get_dir

	Description: Returns the current directory.
		
	Author: Jason Milhaven
		
	History:
		
	==============================================================================
"""

def get_dir():
	return os.getcwd().rsplit("\\", 1)[0] + "\\Python_Four_Week_Rpg\\"

"""
	==============================================================================
	
	Method: get_res

	Description: Returns the resources folder.
		
	Author: Jason Milhaven
		
	History:
		
	==============================================================================
"""
	
def get_res():
	return get_dir() + "resources\\"

"""
	==============================================================================
	
	Method: load_img

	Description: Attempts to load an image in the resources folder, prints an error
	msg upon failure.
		
	Author: Jason Milhaven
		
	History:
		
	==============================================================================
"""
	
def load_img(name):
	ret = None
	fullName = get_res() + name
	
	try:
		ret = pygame.image.load(fullName)
	except Exception:
		print("failed to load image " + fullName)
	return ret

"""
	==============================================================================
	
	Method: load_sound

	Description: Attempts to load an sound in the resources folder, prints an error
	msg upon failure.
		
	Author: Jason Milhaven
		
	History:
		
	==============================================================================
"""
	
def load_sound(name):
	ret = None
	fullName = get_res() + name
	
	try:
		ret = pygame.mixer.Sound(fullName)
	except Exception:
		print("failed to load sound " + fullName)
	return ret

"""
	==============================================================================
	
	Method: load_font

	Description: Attempts to load a font in the resources folder, prints an error
	msg upon failure.
		
	Author: Jason Milhaven
		
	History:
		
	==============================================================================
"""
	
def load_font(name, size):
	ret = None
	fullName = get_res() + name
	
	try:
		ret = pygame.font.Font(fullName, size)
	except Exception:
		print("failed to load font " + fullName)
	return ret

"""
	==============================================================================
	
	Method: clamp01

	Description: "Clamps" any number between 0 and 1.  If 256 is passed through,
	1 is returned.  If -88 is passed through, -1 is returned.  If the argument
	is within 1 to -1, the value returned will not be changed.  Passing 0.745
	will still return 0.745.
		
	Author: Jason Milhaven
		
	History:
		
	==============================================================================
"""

def clamp01(num):
	ret = num

	min = -1
	max = 1

	if num < min:
		ret = min
	elif num > max:
		ret = max

	return ret

"""
	==============================================================================
	
	Method: distance

	Description: Returns distance between two Transforms.
		
	Author: Jason Milhaven
		
	History:
		
	==============================================================================
"""

def distance(self, t1, t2):
	x1 = t1.get_pos_x()
	y1 = t1.get_pos_y()
	x2 = t2.get_pos_x()
	y2 = t2.get_pos_y()
	dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return dist

