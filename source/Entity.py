import time

from enum import *

from utilities import *
from Transform import *
from Tile import *

class EntityState(Enum):
		IDLING = 0
		WALKING = 1
		ATTACKING = 2

class Entity(Transform):

	def __init__(self, posX = 0, posY = 0, sizeX = TILE_SCALE, sizeY = TILE_SCALE):
		super().__init__(posX, posY, sizeX, sizeY)
		
		self.ANIM_WALK_DELAY = 0.2
		
		self.__moveX__ = 0
		self.__moveY__ = 0
		self.maxHealth = 100
		self.__health__ = self.maxHealth
		self.damage = 0
		self.moveSpeed = 100
		self.range = 2
		
		# likely to go unused
		self.strength = 0
		self.dexterity = 0
		self.intellegence = 0
		
		self.__entityState__ = EntityState.IDLING
		self.anims = [
			load_img("e1.png"),
			load_img("e2.png"),
			load_img("e3.png")
		]
		self.lastTime = time.time()

	def get_move_x(self):
		return self.__moveX__
	
	def set_move_x(self, v):
		self.__moveX__ = v
		Entity.check_moving(self)
		#print(self.__entityState__)
	
	def get_move_y(self):
		return self.__moveY__
	
	def set_move_y(self, v):
		self.__moveY__ = v
		Entity.check_moving(self)
	
	def get_move(self):
		return self.get_move_x(), self.get_move_y()
	
	def set_move(self, x, y):
		self.set_move_x(x)
		self.set_move_y(y)
	
	def get_health(self):
		return self.__health__
		
	def set_health(self, v):
		self.__health__ = v
	
	def check_moving(self):
		if abs(self.get_move_x()) + abs(self.get_move_y()) == 0:
			self.__entityState__ = EntityState.IDLING
		else:
			self.__entityState__ = EntityState.WALKING
	
	def animate(self):
		if self.__entityState__ == EntityState.IDLING:
			self.img = self.anims[0]
		if self.__entityState__ == EntityState.WALKING:
			timePassed = time.time() - self.lastTime
			if timePassed >= self.ANIM_WALK_DELAY:
				self.img = self.anims[1]
				self.lastTime = time.time()
		if self.__entityState__ == EntityState.ATTACKING:
			self.img = self.anims[2]
		
	
	def update(self, frameDelta):
		newX = self.get_pos_x() + self.get_move_x() * self.moveSpeed * frameDelta
		newY = self.get_pos_y() + self.get_move_y() * self.moveSpeed * frameDelta
		self.set_pos(newX, newY)
	
	
	def attack(self, enemy):
		self.__entityState__ = EntityState.ATTACKING
		enemy.set_health(enemy.get_health() - self.damage)
