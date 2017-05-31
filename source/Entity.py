import time
import asyncio
#from concurrent.futures import ProcessPoolExecutor
import concurrent.futures

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
        self.attackDelay = 1 #0.2
        print("attackDelay set to 1")
        #self.attackDelayActive = False
        self.attackDelayAccumulator = 0.0
        self.moveSpeed = 250
        self.range = 300
        self.room = room
        
        # likely to go unused
        self.strength = 0
        self.dexterity = 0
        self.intellegence = 0
        
        self.__entityState__ = EntityState.IDLING
        self.anims = [
            load_img("e1.png"),
            load_img("e2.5.png"),
            load_img("e2.png"),
            load_img("e3.png")
        ]
        self.lastTime = time.time()
    
    # getter for moveX
    def get_move_x(self):
        return self.__moveX__
    
    """
        ==============================================================================
        
        Method: set_move_x
        
        Description: set moveX with v clamped between -1 and 1.
        Call check_moving after.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def set_move_x(self, v):
        self.__moveX__ = clamp01(v)
        Entity.__check_moving__(self)
    
    # getter for moveY
    def get_move_y(self):
        return self.__moveY__
    
    """
        ==============================================================================
        
        Method: set_move_y
        
        Description: set moveY with v clamped between -1 and 1.
        Call check_moving after.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def set_move_y(self, v):
        self.__moveY__ = clamp01(v)
        Entity.__check_moving__(self)
    
    # getter for move
    def get_move(self):
        return self.get_move_x(), self.get_move_y()
    
    # setter for move
    def set_move(self, x, y):
        self.set_move_x(x)
        self.set_move_y(y)
        
    # getter for health
    def get_health(self):
        return self.__health__
    
    # setter for health
    def set_health(self, v):
        self.__health__ = v
    
    """
        ==============================================================================
        
        Method: check_moving
        
        Description: If the entity is moving, set state to idle.  Otherwise, set to walking.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def __check_moving__(self):
        if ((abs(self.get_move_x()) + abs(self.get_move_y()) == 0) and self.__entityState__ != EntityState.ATTACKING):
            self.__entityState__ = EntityState.IDLING
        else:
            self.__entityState__ = EntityState.WALKING
    
    """
        ==============================================================================
        
        Method: animate
        
        Description: Set the entity's display image to the image that corresponds to
        the entity's state.  Walking will allow two different images.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def animate(self):
        if self.__entityState__ == EntityState.IDLING:
            self.img = self.anims[0]
        if self.__entityState__ == EntityState.WALKING:
            timePassed = time.time() - self.lastTime
            if timePassed >= self.ANIM_WALK_DELAY:
                self.img = self.anims[1]
                self.lastTime = time.time()
            else:
                self.img = self.anims[2]
        if self.__entityState__ == EntityState.ATTACKING:
            self.img = self.anims[3]
        
    """
        ==============================================================================
        
        Method: delayed_update
        
        Description: Is called at minimum interval of the Program's defined updateDelay,
        but can take longer and is not called at a fixed interval; frameDelta will
        always have a min value, but never less than the value, and sometimes more.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def delayed_update(self, frameDelta):
        pass
        
    """
        ==============================================================================
        
        Method: pre_update
        
        Description: Called by main program in the game loop before update is called, runs before
        collisions are checked.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
        
    def pre_update(self, frameDelta):
        pass
        
    """
        ==============================================================================
        
        Method: update
        
        Description: Called by main program in the game loop, actually changes the position
        of the entity given moveX and moveY.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def update(self, frameDelta):
        self.attackDelayAccumulator += frameDelta
        
        newX = self.get_pos_x() + self.get_move_x() * self.moveSpeed * frameDelta
        newY = self.get_pos_y() + self.get_move_y() * self.moveSpeed * frameDelta
        self.set_pos(newX, newY)
    
    """
        ==============================================================================
        
        Method: wait_attack
        
        Description: Waits the attack delay, is called in attack method to ensure
        that attack cannot be called every frame.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def wait_attack(self, future):
        print("wait attack begin")
        
        #await asyncio.sleep(self.attackDelay)
        #await asyncio.sleep(self.attackDelay)
        
        #self.attackDelayActive = False
        print("moveSpeed is: " + str(self.moveSpeed))
        self.trash()
        print("wait attack end")
    
    """
        ==============================================================================
        
        Method: attack
        
        Description: Attacks a given target, sets state to attacking.
        Will check to see if enemy is in the entity's attack range.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def attack(self, enemy):
        #print(self.attackDelayActive)
        if (self.attackDelayAccumulator >= self.attackDelay) and (distance(self, enemy) <= self.range):
            self.attackDelayAccumulator = 0.0
            #print("is there lag yet?")
            
            print(1)
            #loop = asyncio.get_event_loop()
            #loop.run_until_complete(self.wait_attack());
            #loop.close()
            
            #pool = ProcessPoolExecutor(3)
            #pool.submit(self.wait_attack)
            #pool.submit(Entity.wait_attack, (self))
            
            #loop = asyncio.get_event_loop()
            #future = asyncio.Future()
            #asyncio.ensure_future(self.wait_attack(future))
            #loop.run_until_complete(future)
            print(2)
            
            self.__entityState__ = EntityState.ATTACKING
            enemy.set_health(enemy.get_health() - self.damage)
