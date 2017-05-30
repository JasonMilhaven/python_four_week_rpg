

from Transform import *
from utilities import *

"""
    ******************************************************************************

    Class: Input
    
    Description: A subclass of Transform, is not intended to be added to the game
    as a "Sprite", and cannot be resized.  The x and y position represent the player's
    input on the W, A, S and D keys to move around, the Input object's position values
    are locked between -1 and 1, with 0 being a possible value.
    -1 is backward, 0 is stand still, and 1 is forward.
    
    Author: Jason Milhaven
    
    History: 
    
    ******************************************************************************
"""

class Input(Transform):

    """
        ==============================================================================
        
        Method: init
        
        Description: Calls base contructor.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """

    def __init__(self):
        super().__init__()

    # setter for posX, value is clamped between -1 and 1
    def set_pos_x(self, v):
        self._posX_ = clamp01(v)
        
    # setter for posY, value is clamped between -1 and 1
    def set_pos_y(self, v):
        self._posY_ = clamp01(v)    

    
    # no reason to increase size of instance
    # setters do nothing
    
    # setter for sizeX
    def set_size_x(self, v):
        pass
    
    # setter for sizeY
    def set_size_x(self, v):
        pass