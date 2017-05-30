
from Entity import *
from utilities import *

"""
    ******************************************************************************

    Class: Monster
    
    Description: Represents a monster Entity in a game.  Monsters will move in a
    set of offsets until a player is found.
    
    Author: Jason Milhaven
    
    History:
    
    ******************************************************************************
"""

class Monster(Entity):
    
    """
        ==============================================================================
        
        Method: init
        
        Description: Defaults the monster sight radius to 5, which will be the threshold
        for where the monster "sees" the player and attacks them.  Assigns instance variables
        to track the monsters' current offset, distance from offset, and starting point.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def __init__(self, posX = 0, posY = 0, room = None):
        if type(self) == Monster:
            raise TypeError("please use the TestMonster class instead of direct Monster instantiation")
        super().__init__(posX, posY, room)
        
        self.sightRange = 100
        self.offsets = [
            (100, 0),
            (0, 100),
            (-100, 0),
            (0, -100)
        ]
        self.__offsetStartingPoint__ = self.get_pos()
        self.__currentOffset__ = 0
        self.__totalOffsetsCompleted__ = 0
        self.target = None
        self.room = room
        
        if self.room:
            self.room.entities.append(self)
        
    """
        ==============================================================================
        
        Method: set_pos_x
        
        Description: Overrides base set_pos_x.  Changes the x position coordinate as well
        as the offsetStartingPoint x coordinate.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
        
    def set_pos_x(self, v):
        #self.__offsetStartingPoint__ = (v, self.__offsetStartingPoint__[1])
        super().set_pos_x(v)
        
    """
        ==============================================================================
        
        Method: set_pos_y
        
        Description: Same as above, but for the y-axis.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
        
    def set_pos_y(self, v):
        #self.__offsetStartingPoint__ = (self.__offsetStartingPoint__[0], v)
        super().set_pos_y(v)
        
    """
        ==============================================================================
        
        Method: _on_offset_completed_
        
        Description: Method desgined to be overridden and implemented in subclasses for
        special cases.  The method is called when the monster completes a movement command.
        This can be used for special monsters to perform an action after moving.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
        
    def _on_offset_completed_(self, completedIndex, newIndex, totalOffsetsCompleted):
        # wtf is this trash
        #print("offset completed")
        #raise NotImplementedError("use this for Monster subclasses")
        pass
        
    """
        ==============================================================================
        
        Method: next_offset
        
        Description: Increments the offset if valid, otherwise resets the offset.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
        
    def next_offset(self):
        self.__totalOffsetsCompleted__ += 1
        completedIndex = self.__currentOffset__
    
        self.__offsetStartingPoint__ = self.get_pos()
        if self.__currentOffset__ >= len(self.offsets) - 1:
            self.__currentOffset__ = 0
        else:
            self.__currentOffset__ += 1
        
        newIndex = self.__currentOffset__
        self._on_offset_completed_(completedIndex, newIndex, self.__totalOffsetsCompleted__)
    
    # comment this when done
    def try_offset(self):
        xStart = self.__offsetStartingPoint__[0]
        yStart = self.__offsetStartingPoint__[1]
        
        xOff = self.offsets[self.__currentOffset__][0]
        yOff = self.offsets[self.__currentOffset__][1]
        
        xPos = self.get_pos_x()
        yPos = self.get_pos_y()
        
        if (abs(xPos - xStart) > abs(xOff) or abs(yPos - yStart) > abs(yOff)):
            self.next_offset()
        
        """if distance(self, self.room.player) <= self.__sightRadius__:
            self.set_move_x(self.room.player.get_pos_x() - self.get_pos_x())
            self.set_move_y(self.room.player.get_pos_y() - self.get_pos_y())"""
        
        a = self.offsets[self.__currentOffset__]
        self.set_move(a[0], a[1])
    
    """
        ==============================================================================
        
        Method: try_attack
        
        Description: Check for player position, if the player is within the sightRange
        field of this instance, move towards and attack player.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def try_attack(self):
        # update this conditional with a list of enemies
        # if monsters should ever attack each other?
        if distance(self, self.room.player) <= self.sightRange:
            self.target = self.room.player
        else:
            self.target = None
            
        if (self.target):
            self.attack(self.target)
            self.set_move(self.target.get_pos_x() - self.get_pos_x(), self.target.get_pos_y() - self.get_pos_y())
    
    """
        ==============================================================================
        
        Method: pre_update
        
        Description: Override base class pre_update to try to attack the player.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def pre_update(self, frameDelta):
        super().pre_update(frameDelta)
    
        self.try_offset()
        self.try_attack()
        
    """
        ==============================================================================
        
        Method: update
        
        Description: If the monster has completed movement of its' current offset,
        call next_offset.  Check if the player is in sightRange for attack.  Move the player
        in the direction of the current offset.
        Calls the base class update.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def update(self, frameDelta):
        super().update(frameDelta)
        
        # if the polarity of the current x offset is not equal to move x
        # or the condition applies on the y-axis
        if (get_polarity_of(self.offsets[self.__currentOffset__][0]) != self.get_move_x() or get_polarity_of(self.offsets[self.__currentOffset__][1]) != self.get_move_y()):
            self.next_offset()