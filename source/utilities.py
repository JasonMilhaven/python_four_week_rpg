import os

import pygame

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (35, 34, 34)

def load_img(name):
	ret = None
	fullName = os.getcwd() + "\\" + name
	try:
		ret = pygame.image.load(fullName).convert()
	except Exception:
		print("failed to load " + fullName)
	return ret

def load_sound(name):
	pass

def clampInputAxis(num):
	ret = num

	min = -1
	max = 1

	if num < min:
		ret = min
	elif num > max:
		ret = max

	return ret