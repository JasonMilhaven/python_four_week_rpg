import os

import pygame

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (35, 34, 34, 0.5)

def get_res():
	return os.getcwd().rsplit("\\", 1)[0] + "\\Python_Four_Week_Rpg\\resources\\"

def load_img(name):
	ret = None
	fullName = get_res() + name
	
	try:
		ret = pygame.image.load(fullName)
	except Exception:
		print("failed to load image " + fullName)
	return ret

def load_sound(name):
	ret = None
	fullName = get_res() + name
	
	try:
		ret = pygame.mixer.Sound(fullName)
	except Exception:
		print("failed to load sound " + fullName)
	return ret

def load_font(name, size):
	ret = None
	fullName = get_res() + name
	
	try:
		ret = pygame.font.Font(fullName, size)
	except Exception:
		print("failed to load font " + fullName)
	return ret
		
	
def clamp01(num):
	ret = num

	min = -1
	max = 1

	if num < min:
		ret = min
	elif num > max:
		ret = max

	return ret