import pygame

from Transform import *
from utilities import *

"""
    ******************************************************************************

    Class: UIComponent
    
    Description: Extend from this class and override the methods
    or set the callback functions upon instantiation, either works ok.
    
    Author: Jason Milhaven
    
    History:
    
    ******************************************************************************
"""

class UIComponent(Transform):

    """
        ==============================================================================
        
        Method: __init__
        
        Description: Constructor for UIComponent class, calls superclass constructor.
        Provides fields to be modified, and events which can be set to functions.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """

    def __init__(self, posX = 0, posY = 0, sizeX = 0, sizeY = 0):
        super().__init__(posX, posY, sizeX, sizeY)
        
        self.__visible__ = True
        self.color = GRAY
        self.borderColor = WHITE
        self.borderSize = 2
        
        self.set_visible_func = None
        self.on_clicked_func = None
        self.on_hover_begin_func = None
        self.on_hover_end_func = None
        
        
    def get_visible(self):
        return self.__visible__
    
    def set_visible(self, v):
        self.__visible__ = v
        if self.set_visible_func:
            self.set_visible_func()
    
    def on_clicked(self):
        if self.on_clicked_func:
            self.on_clicked_func()
        
    def on_hover_begin(self):
        if self.on_hover_begin_func:
            self.on_hover_begin_func()
        
    def on_hover_end(self):
        if self.on_hover_end_func:
            self.on_hover_end_func()

