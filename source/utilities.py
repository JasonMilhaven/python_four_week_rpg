import os

import pygame

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def load_img(name):
	ret = None
	fullName = os.getcwd() + "\\" + name
	try:
		ret = pygame.image.load(fullName).convert()
	except Exception:
		print("failed to load " + fullName)
	return ret