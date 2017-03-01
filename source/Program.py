#import time
import threading
import sys
import os

import pygame

from UIComponent import *
from utilities import *

def test():
	print("test works")

class Program():

	def __init__(self):
		
		# constants
		self.WIN_TITLE = "RPG_Title"
		self.WIN_WIDTH = 1024
		self.WIN_HEIGHT = 576
		self.WIN_ICON_FILENAME = "\\Icon.png"
		
		self.FILL_COLOR = (0, 0, 0)
		
		# core variables
		self.isRunning = True
		self.isInGame = False
		self.uiComponents = []
		
		# in game
		self.player = None
		self.entities = []
		
		# pygame initialization
		pygame.init()
		
		self.pygameSurface = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
		pygame.display.set_caption(self.WIN_TITLE)
		pygame.display.set_icon(load_img(self.WIN_ICON_FILENAME))
		
		# make the ui
		u = UIComponent()
		u.set_pos(400, 400)
		u.set_size(100, 100)
		u.onClicked = test
		self.uiComponents.append(u)
		
		u2 = UIComponent()
		u2.set_pos(380, 380)
		u2.set_size(100, 100)
		self.uiComponents.append(u2)
		
		# begin the main program
		
		self.drawThread = threading.Thread(target=self.draw_loop)
		self.drawThread.setDaemon(True)
		self.drawThread.start()
		self.event_loop()

	def __is_mouse_over__(self, mX, mY, transform):
		ret = False
		
		xCondition = mX <= transform.get_pos_x() + transform.get_size_x() and mX > transform.get_pos_x()
		yCondition = mY <= transform.get_pos_y() + transform.get_size_y() and mY > transform.get_pos_y()
		
		ret = xCondition and yCondition
		return ret
	
	def event_loop(self):
		while self.isRunning:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.isRunning = False
					pygame.quit()
					sys.exit(0)
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mX = event.pos[0]
					mY = event.pos[1]
					
					clickedUI = None
					
					# REVERSE the ui click detection, very important
					for ui in reversed(self.uiComponents):
						if self.__is_mouse_over__(mX, mY, ui):
							clickedUI = ui
							break
					
					if clickedUI:
						clickedUI.on_clicked()
					
					"""for entity in self.entities:
						if self.__is_mouse_over__(mX, mY, ui):
							print("mouse clicked an entity")"""

	def __draw_transform__(self, transform):
		pygame.draw.rect(self.pygameSurface, transform.color, (
			transform.get_pos_x(),
			transform.get_pos_y(),
			transform.get_size_x(),
			transform.get_size_y()
		))
	
	def __draw_ui__(self, ui):
		self.__draw_transform__(ui)
		
		pygame.draw.rect(self.pygameSurface, ui.borderColor, (
			ui.get_pos_x(),
			ui.get_pos_y(),
			ui.get_size_x(),
			ui.borderSize
		))
		pygame.draw.rect(self.pygameSurface, ui.borderColor, (
			ui.get_pos_x(),
			ui.get_pos_y() + ui.get_size_y() - ui.borderSize,
			ui.get_size_x(),
			ui.borderSize
		))
		pygame.draw.rect(self.pygameSurface, ui.borderColor, (
			ui.get_pos_x(),
			ui.get_pos_y(),
			ui.borderSize,
			ui.get_size_y()
		))
		pygame.draw.rect(self.pygameSurface, ui.borderColor, (
			ui.get_pos_x() + ui.get_size_x() - ui.borderSize,
			ui.get_pos_y(),
			ui.borderSize,
			ui.get_size_y()
		))
		
	
	def draw_loop(self):
		while self.isRunning:
			self.pygameSurface.fill(self.FILL_COLOR)
			
			for ui in self.uiComponents:
				self.__draw_ui__(ui)
			
			for entity in self.entities:
				self.__draw_transform__(entity)
			
			pygame.display.update()
