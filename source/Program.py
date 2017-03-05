import time
import math
import threading
import sys
import os

import pygame

from Entity import *
from Player import *
from UIComponent import *
from UITextComponent import *
from Input import *
from Tile import *
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
		self.RENDER_DISTANCE = 1440
		
		# core variables
		self.isRunning = True
		self.isInGame = False
		self.uiComponents = []
		self.hoveredUI = None
		self.input = Input()
		self.lastTime = time.time()
		
		# in game
		self.entities = []
		self.tiles = []
		
		#self.player = None
		# THIS IS A PLACEHOLDER FIX THIS AFTER TESTING <---------------------------------------
		self.player = Player()
		self.entities.append(self.player)
		
		# pygame initialization
		pygame.init()
		
		self.pygameSurface = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
		pygame.display.set_caption(self.WIN_TITLE)
		pygame.display.set_icon(load_img(self.WIN_ICON_FILENAME))
		
		# make the ui
		u = UITextComponent(380, 200, 100, 100)
		u.set_visible(False)
		u.name = "UI 1"
		u.text = "test"
		u.borderSize = 1
		self.uiComponents.append(u)
		
		u2 = UIComponent(400, 400, 100, 100)
		u2.set_visible(False)
		u2.name = "UI 2"
		self.uiComponents.append(u2)
		
		b = UIComponent(400, 100, 300, 100)
		b.set_visible(False)
		b.name = "Banner"
		b.img = load_img("TestBanner.png")
		self.uiComponents.append(b)
		
		# test game objects
		
		t = Tile(200, 200)
		t.isBlocking = True
		t.img = load_img("TestTile.png")
		self.tiles.append(t)
		
		self.create_initial_tiles()
		
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
		
	
	def create_initial_tiles(self):
		
		a = int(self.WIN_WIDTH / TILE_SCALE)
		b = int(self.WIN_HEIGHT / TILE_SCALE)
		
		for x in range(-20, 20):
			for y in range(-20, 20):
				t = Tile(x * TILE_SCALE, y * TILE_SCALE)
				t.img = load_img("TestTile.png")
				self.tiles.append(t)


	def __is_in__(self, mX, mY, transform):
		
		ret = False
		
		xCondition = mX <= transform.get_pos_x() + transform.get_size_x() * 0.5 and mX > transform.get_pos_x() - transform.get_size_x() * 0.5
		yCondition = mY <= transform.get_pos_y() + transform.get_size_y() * 0.5 and mY > transform.get_pos_y() - transform.get_size_y() * 0.5
		
		ret = xCondition and yCondition
		return ret
		

	def __colliding_x__(self, t1, t2):
		ret = False
		
		len = abs(t1.get_size_x() * 0.5 + t2.get_size_x() * 0.5)
		
		if abs(t1.get_pos_x() - t2.get_pos_x()) < len:
			ret = True
		
		return ret

		
	def __colliding_y__(self, t1, t2):
		ret = False
		
		len = abs(t1.get_size_y() * 0.5 + t2.get_size_y() * 0.5)
		
		if abs(t1.get_pos_y() - t2.get_pos_y()) < len:
			ret = True
		
		return ret
		
		
	def __distance__(self, t1, t2):
		x1 = t1.get_pos_x()
		y1 = t1.get_pos_y()
		x2 = t2.get_pos_x()
		y2 = t2.get_pos_y()
		dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
		return dist
		
	
	def event_loop(self):
		while self.isRunning:
			print("make a framerate cap for both loops")
			# print(self.input.get_pos_x(), self.input.get_pos_y())
		
			mX, mY = pygame.mouse.get_pos()
			
			# get the time between frame
			
			frameDelta = time.time() - self.lastTime
			self.lastTime = time.time()
			
			for ui in self.uiComponents:
				if ui.get_visible():
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
						if ui.get_visible():
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
						self.input.set_pos_y(-1)
					elif rawKey == pygame.K_a:
						self.input.set_pos_x(-1)
					elif rawKey == pygame.K_s:
						self.input.set_pos_y(1)
					elif rawKey == pygame.K_d:
						self.input.set_pos_x(1)
					
					
				elif event.type == pygame.KEYUP:
				
					rawKey = event.key
						
					if rawKey == pygame.K_w:
						self.input.set_pos_y(self.input.get_pos_y() + 1)
					elif rawKey == pygame.K_a:
						self.input.set_pos_x(self.input.get_pos_x() + 1)
					elif rawKey == pygame.K_s:
						self.input.set_pos_y(self.input.get_pos_y() - 1)
					elif rawKey == pygame.K_d:
						self.input.set_pos_x(self.input.get_pos_x() - 1)
			
			# set player move to input
			if self.player:
				self.player.set_move(self.input.get_pos_x(), self.input.get_pos_y())
				
			
			# ensure entities cannot walk into tiles
			for entity in self.entities:
				for tile in self.tiles:
					if tile.isBlocking:
						if self.__colliding_x__(entity, tile) and self.__colliding_y__(entity, tile):
							if entity.get_move_x() == clamp01(tile.get_pos_x() - entity.get_pos_x()):
								entity.set_move_x(0)
							if entity.get_move_y() == clamp01(tile.get_pos_y() - entity.get_pos_y()):
								entity.set_move_y(0)

			entity.update(frameDelta)
			entity.animate()
	
	def __draw_ui__(self, ui):
		pygame.draw.rect(self.pygameSurface, ui.color, (
			ui.get_pos_x() - (ui.get_size_x() * 0.5),
			ui.get_pos_y() - (ui.get_size_y() * 0.5),
			ui.get_size_x(),
			ui.get_size_y()
		))
		
		pygame.draw.rect(self.pygameSurface, ui.borderColor, (
			ui.get_pos_x() - (ui.get_size_x() * 0.5),
			ui.get_pos_y() - (ui.get_size_y() * 0.5),
			ui.get_size_x(),
			ui.borderSize
		))
		pygame.draw.rect(self.pygameSurface, ui.borderColor, (
			ui.get_pos_x() - (ui.get_size_x() * 0.5),
			ui.get_pos_y() - (ui.get_size_y() * 0.5) + ui.get_size_y() - ui.borderSize,
			ui.get_size_x(),
			ui.borderSize
		))
		pygame.draw.rect(self.pygameSurface, ui.borderColor, (
			ui.get_pos_x() - (ui.get_size_x() * 0.5),
			ui.get_pos_y() - (ui.get_size_y() * 0.5),
			ui.borderSize,
			ui.get_size_y()
		))
		pygame.draw.rect(self.pygameSurface, ui.borderColor, (
			ui.get_pos_x() - (ui.get_size_x() * 0.5) + ui.get_size_x() - ui.borderSize,
			ui.get_pos_y() - (ui.get_size_y() * 0.5),
			ui.borderSize,
			ui.get_size_y()
		))
	
	# use offset getters because the draw thread
	# is sometimes too fast if you store the result in a variable
	
	def get_x_off(self):
		return self.WIN_WIDTH * 0.5 - self.player.get_pos_x()
	
	
	def get_y_off(self):
		return self.WIN_HEIGHT * 0.5 - self.player.get_pos_y()
		
	
	def draw_loop(self):
		while self.isRunning:
			self.pygameSurface.fill(self.FILL_COLOR)			
			
			if self.player:
				xOff = self.get_x_off()
				yOff = self.get_y_off()
				
				for tile in self.tiles:
					if self.__distance__(self.player, tile) <= self.RENDER_DISTANCE:
						tile.draw(self.pygameSurface, self.get_x_off(), self.get_y_off())
				for entity in self.entities:
					if self.__distance__(self.player, entity) <= self.RENDER_DISTANCE:
						if entity == self.player:
							#entity.draw(self.pygameSurface, self.WIN_WIDTH * 0.5 - self.player.get_pos_x(), self.WIN_HEIGHT * 0.5 - self.player.get_pos_y())
							#entity.draw(self.pygameSurface, xOff, yOff)
							entity.draw(self.pygameSurface, self.get_x_off(), self.get_y_off())
						else:
							entity.draw(self.pygameSurface, self.get_x_off(), self.get_y_off())
				
			for ui in self.uiComponents:
				if ui.get_visible():
					self.__draw_ui__(ui)
					ui.draw(self.pygameSurface);
			
			pygame.display.update()
