
from Transform import *

TILE_SCALE = 32

"""
    ******************************************************************************

    Class: Tile
    
    Description: 
    
    Author: Jason Milhaven
    
    History:
    
    ******************************************************************************
"""

class Tile(Transform):
    
    """
        ==============================================================================
        
        Method: __init__
        
        Description: Constructor for Room class, calls superclass constructor.
        Defaults to non-blocking and loads the default image.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def __init__(self, posX = 0, posY = 0, sizeX = TILE_SCALE, sizeY = TILE_SCALE):
        super().__init__(posX, posY, sizeX, sizeY)
        
        self.isBlocking = False
        self.img = load_img("Grass.png")
    
    
    def set_size_x(self, x):
        __x__ = TILE_SCALE
    
    def set_size_y(self, y):
        __Y__ = TILE_SCALE