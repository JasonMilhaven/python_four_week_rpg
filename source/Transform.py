
from utilities import *

"""
    ******************************************************************************

    Class: Transform
    
    Description: Represents a two-dimensional container for any object in the game.
    
    Author: Jason Milhaven
    
    History:
    
    ******************************************************************************
"""

class Transform():

    """
        ==============================================================================
        
        Method: __init__
        
        Description: Constructor for Transform, prevents direct base class
        instantiation.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """

    def __init__(self, posX = 0, posY = 0, sizeX = 0, sizeY = 0):
        if type(self) == Transform:
            raise TypeError("do not instantiate a Transform directly")
        self.name = ""
        self._posX_ = posX
        self._posY_ = posY
        self._sizeX_ = sizeX
        self._sizeY_ = sizeY
        
        self.img = None
    
    # single field accessors
    
    # getter for posX
    def get_pos_x(self):
        return self._posX_
    
    # setter for posX
    def set_pos_x(self, v):
        self._posX_ = v
        
    # getter for posY
    def get_pos_y(self):
        return self._posY_
        
    # setter for posY
    def set_pos_y(self, v):
        self._posY_ = v
    
    # getter for sizeX
    def get_size_x(self):
        return self._sizeX_
    
    # setter for sizeX
    def set_size_x(self, v):
        self._sizeX_ = v
        
    # getter for sizeY
    def get_size_y(self):
        return self._sizeY_
        
    # setter for sizeY
    def set_size_y(self, v):
        self._sizeY_ = v
    
    # multiple field accessors
    
    # getter for pos
    def get_pos(self):
        return (self.get_pos_x(), self.get_pos_y())
    
    # setter for pos
    def set_pos(self, x, y):
        self.set_pos_x(x)
        self.set_pos_y(y)
    
    # getter for size
    def get_size(self):
        return (self.get_size_x(), self.get_size_y())
    
    # setter for size
    def set_size(self, x, y):
        self.set_size_x(x)
        self.set_size_y(y)
        
    """
        ==============================================================================
        
        Method: draw
        
        Description: Accepts a pyGame Screen instance, if the transform has an image,
        the image is drawn to the screen at self's position and size.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def draw(self, screen):
        if self.img:
            screen.blit(self.img.convert_alpha(), (self.get_pos_x() - self.get_size_x() * 0.5, self.get_pos_y() - self.get_size_y() * 0.5))
            
            