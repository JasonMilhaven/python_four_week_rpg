#import time
import threading
import sys
import os

import pygame

from UIComponent import *
from Input import *
from utilities import *

"""
	******************************************************************************

	Class: Program
	
	Description: A single instance class representing the program, with a window,
	draw loop, and game loop to handle logic.
	
	Author: Jason Milhaven
	
	History: No longer using "Daemon" thread as draw loop,
	draw loop should be terminated first, not last.
	
	******************************************************************************
"""

class Program():

	"""
		==============================================================================
		
		Method: __init__
		
		Description: Constructor for the Program class, creates the window given
		a title, w and h constants, sets window icon.
		
		The game logic and event handling is in event_loop, on the main thread.
		The drawing is handled exclusively in draw_loop, on a seperate thread.
		
		UI is created upon instantiation.
		
		Author: Jason Milhaven
		
		History:
		
		==============================================================================
	"""

	def __init__(self):
		
		# constants
		self.WIN_TITLE = "Pythonica"
		self.WIN_WIDTH = 1024
		self.WIN_HEIGHT = 576
		self.WIN_ICON_FILENAME = "Icon.png"
		self.FILL_COLOR = (0, 0, 0)
		
		# core variables
		self.isRunning = True
		self.isInGame = False
		self.uiComponents = []
		self.hoveredUI = None
		self.input = Input()
		
		# in game
		self.player = None
		self.entities = []
		self.tiles = []
		
		# pygame initialization
		pygame.init()
		
		self.pygameSurface = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
		pygame.display.set_caption(self.WIN_TITLE)
		pygame.display.set_icon(load_img(self.WIN_ICON_FILENAME))
		
		# make the ui
		u = UIComponent()
		u.name = "UI 1"
		u.set_pos(380, 380)
		u.set_size(100, 100)
		self.uiComponents.append(u)
		
		u2 = UIComponent()
		u2.name = "UI 2"
		u2.set_pos(400, 400)
		u2.set_size(100, 100)
		self.color = GRAY
		self.borderColor = WHITE
		self.uiComponents.append(u2)
		
		# begin the main program
		
		self.drawThread = threading.Thread(target=self.draw_loop)
		#self.drawThread.setDaemon(True)
		# threads should be killed manually
		self.drawThread.start()
		self.event_loop()

	def close(self):
		self.isRunning = False
		
		# kill any threads here
		self.drawThread.join()
		
		pygame.quit()
		sys.exit(0)

	def __is_in__(self, mX, mY, transform):
		ret = False
		
		xCondition = mX <= transform.get_pos_x() + transform.get_size_x() and mX > transform.get_pos_x()
		yCondition = mY <= transform.get_pos_y() + transform.get_size_y() and mY > transform.get_pos_y()
		
		ret = xCondition and yCondition
		return ret
	
	"""def __in_tile__(self, x, y, tile):
		ret = False
		
		xCondition = x <= tile.get_pos_x() + tile.get_size_x() and x > tile.get_pos_x()
		xCondition = y <= tile.get_pos_y() + tile.get_size_y() and y > tile.get_pos_y()
		
		ret = xCondition"""
	
	def event_loop(self):
		while self.isRunning:
			#print(self.input.get_pos_x(), self.input.get_pos_y())
		
			mX, mY = pygame.mouse.get_pos()
		
			for ui in self.uiComponents:
				if self.hoveredUI:
					if not self.__is_in__(mX, mY, self.hoveredUI):
						self.hoveredUI.on_hover_end()
						self.hoveredUI = None
					break
				else:
					if self.__is_in__(mX, mY, ui):
						self.hoveredUI = ui
						ui.on_hover_begin()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.close()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					clickedUI = None
					
					# REVERSE the ui click detection, very important
					for ui in reversed(self.uiComponents):
						if self.__is_in__(mX, mY, ui):
							clickedUI = ui
							ui.on_clicked()
							break
					
					#if clickedUI:
					#	clickedUI.on_clicked()
					
					"""for entity in self.entities:
						if self.__is_in__(mX, mY, ui):
							print("mouse clicked an entity")"""
							
				elif event.type == pygame.KEYDOWN:
				
					rawKey = event.key
					prettyKey = event.unicode
					
					if rawKey == pygame.K_w:
						self.input.set_pos_y(1)
					elif rawKey == pygame.K_a:
						self.input.set_pos_x(-1)
					elif rawKey == pygame.K_s:
						self.input.set_pos_y(-1)
					elif rawKey == pygame.K_d:
						self.input.set_pos_x(1)
					
				elif event.type == pygame.KEYUP:
				
					rawKey = event.key
					
					if rawKey == pygame.K_w:
						self.input.set_pos_y(0)
					elif rawKey == pygame.K_a:
						self.input.set_pos_x(0)
					elif rawKey == pygame.K_s:
						self.input.set_pos_y(0)
					elif rawKey == pygame.K_d:
						self.input.set_pos_x(0)
			
			# ensure entities cannot walk into tiles
			for entity in self.entities:
				for tile in self.tiles:
					if self.__is_in__(entity.get_move() + entity.get_pos):
						entity.set_move(-entity.moveX, -entity.moveY)

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
