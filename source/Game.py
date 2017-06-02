

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
        
        Method: init
        
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
        
        self.width = width
        self.height = height
        
        self.new_room()
        
    """
        ==============================================================================
        
        Method: new_room
        
        Description: Creates a room given self's width and height, the new room object
        is set to the current room and appended to the room list for serialization.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """

    def new_room(self):
        print("NEW ROOM CREATED")
        r = Room(self.width, self.height, self.player)
        self.rooms.append(r)
        self.currentRoom = r
        
        