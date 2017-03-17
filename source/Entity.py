import time

from enum import *

from Transform import *
from Tile import *
from utilities import *

"""
    ******************************************************************************

    Enum: EntityState
    
    Description: Not technically a Class, but an Enumeration.  Contains static members
    as ints which represent the "state" of an entity: idling, walking, or attacking.
    Animations will be played base on the entity's state, if there is time.
    
    Author: Jason Milhaven
    
    History: 
    
    ******************************************************************************
"""

class EntityState(Enum):
        IDLING = 0
        WALKING = 1
        ATTACKING = 2


"""
    ******************************************************************************

    Class: Entity
    
    Description: Has the characteristics of a live object in the game, will move
    around, attack, has damage and health, and the potential to die.  Will
    be subclassed by Player and Monster, as well as various specific Monsters.
    Animations should be loaded in the base class constructor, as well as any
    unique values for health/dmg.
    
    Author: Jason Milhaven
    
    History: 
    
    ******************************************************************************
"""
        
class Entity(Transform):

    """
        ==============================================================================
        
        Method: init
        
        Description: Constructor for the Entity class, defines property backends for
        movement, defines maxHealth, damage, moveSpeed, range, and the current room.
        Defines the "state" of the Entity, which is either idling, walking, or attacking
        based on movement and/or attack method calls.
        
        Loads default animation images, this class should not be directly instantiated,
        yet will not error out if it is.
        
        Strength, dexterity, and intellegence are likely to go unused.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """

    #def __init__(self, posX = 0, posY = 0, sizeX = TILE_SCALE, sizeY = TILE_SCALE):
    def __init__(self, posX = 0, posY = 0, room = None):
        super().__init__(posX, posY, sizeX = TILE_SCALE - 4, sizeY = TILE_SCALE - 4)
        
        self.ANIM_WALK_DELAY = 0.2
        
        self.__moveX__ = 0
        self.__moveY__ = 0
        self.maxHealth = 100
        self.__health__ = self.maxHealth
        self.damage = 0
        self.moveSpeed = 250 #500
        self.range = 2
        self.room = room
        
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

    """
        ==============================================================================
        
        Method: 
        
        Description: Constructor for the Entity class, defines property backends for
        movement, defines maxHealth, damage, moveSpeed, range, and the current room.
        Defines the "state" of the Entity, which is either idling, walking, or attacking
        based on movement and/or attack method calls.
        
        Loads default animation images, this class should not be directly instantiated,
        yet will not error out if it is.
        
        Strength, dexterity, and intellegence are likely to go unused.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def get_move_x(self):
        return self.__moveX__
    
    def set_move_x(self, v):
        self.__moveX__ = clamp01(v)
        Entity.__check_moving__(self)
    
    def get_move_y(self):
        return self.__moveY__
    
    def set_move_y(self, v):
        self.__moveY__ = clamp01(v)
        Entity.__check_moving__(self)
    
    def get_move(self):
        return self.get_move_x(), self.get_move_y()
    
    def set_move(self, x, y):
        self.set_move_x(x)
        self.set_move_y(y)
    
    def get_health(self):
        return self.__health__
        
    def set_health(self, v):
        self.__health__ = v
    
    def __check_moving__(self):
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
