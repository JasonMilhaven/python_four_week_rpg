from enum import *
from utilities import *

class Entity(Transform):
    
    class EntityState(Enum):
		IDLING = 0
		WALKING = 1
		ATTACKING = 2

	def __init__(self):
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
        
	def animate():
		pass
	
	def update():
		pass