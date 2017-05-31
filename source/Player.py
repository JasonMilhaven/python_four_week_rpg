

from Entity import *

"""
    ******************************************************************************

    Class: Player
    
    Description: Represents the player Entity in a game.
    
    Author: Jason Milhaven
    
    History:
    
    ******************************************************************************
"""

class Player(Entity):

    """
        ==============================================================================
        
        Method: init
        
        Description: Constructor for Player class, loads Player textures as animations.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """

    def __init__(self, posX = TILE_SCALE * 0.5, posY = TILE_SCALE * 0.5, room = None):
        super().__init__(posX, posY, room)
        
        self.anims[0] = load_img("player.png")
        self.anims[1] = load_img("walking.png")
        
        
    def delayed_update(self, frameDelta):
        super().delayed_update(frameDelta)
    