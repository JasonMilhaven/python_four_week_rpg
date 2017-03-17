

from Player import *
from Room import *

"""
    ******************************************************************************

    Class: Game
    
    Description: Represents a "save" file, which will be loaded and modified by the
    Program.  Instances of this class will be saved and loaded through the Python
    Pickle library at the menu screen.
    
    Author: Jason Milhaven
    
    History: 
    
    ******************************************************************************
"""

class Game():

    """
        ==============================================================================
        
        Method: __init__
        
        Description: Constructor for the Game class, will create rooms given the width
        and height.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """

    def __init__(self, width, height):
        self.username = "?????"
        self.rooms = []
        self.player = Player()
        
        self.rooms.append(Room(width, height, self.player))
        self.currentRoom = self.rooms[0]