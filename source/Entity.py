from enum import *
from utilities import *

class Entity(Transform):
    
    class EntityState(Enum):
		IDLING = 0
		WALKING = 1
		ATTACKING = 2

	def __init__(self):
		self.moveX = 0
		self.moveY = 0
		self.maxHealth = 0
		self.health= self.maxHealth
		self.damage = 0
		self.moveSpeed = 0
		self.range = 0
		self.strength = 0
		self.dexterity = 0
		self.intellegence = 0
		self.__entityState__ = EntityState.IDLING
		self.anims = []
        
	def get_move():
		return moveX, moveY
	
	def animate():
		pass
	
	def update():
		pass