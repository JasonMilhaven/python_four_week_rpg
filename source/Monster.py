
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
    
    def __init__(self, posX = 0, posY = 0, room = None):
        if type(self) == Monster:
            raise TypeError("please use the TestMonster class instead of direct Monster instantiation")
        super().__init__(posX, posY, room)
        
        self.__sightRadius__ = 5
        self.__offsets__ = [
            (5, 0),
            (0, 5),
            (-5, 0),
            (0, -5)
        ]
        self.__offsetStartingPoint__ = self.get_pos()
        self.__currentOffset__ = 0
        self.room = room
        
        if self.room:
            self.room.entities.append(self)
        
        
    def next_offset(self):
        if self.__currentOffset__ >= len(self.__offsets__) - 1:
            self.__currentOffset__ = 0
        else:
            self.__currentOffset__ += 1
        
    
    def update(self, frameDelta):       
        if self.get_pos_x() >= self.__offsetStartingPoint__[0] + self.__offsets__[self.__currentOffset__][0] and self.get_pos_y() >= self.__offsetStartingPoint__[1] + self.__offsets__[self.__currentOffset__][1]:
            self.next_offset()
        
        #if self.get_move_x() == 0 and self.get_move_y() == 0:
        #   self.next_offset()
        
        """if distance(self, self.room.player) <= self.__sightRadius__:
            self.set_move_x(self.room.player.get_pos_x() - self.get_pos_x())
            self.set_move_y(self.room.player.get_pos_y() - self.get_pos_y())"""
        
        if distance(self, self.room.player) <= self.range:
            self.attack(self.room.player)
        
        a = self.__offsets__[self.__currentOffset__]
        self.set_move(a[0], a[1])
        
        super().update(frameDelta)
        