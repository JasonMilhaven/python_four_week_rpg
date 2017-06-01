

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
        
    """
        ==============================================================================
        
        Method: delayed_update
        
        Description: Override delayed_update, currently does nothing.
        
        Author: Jason Milhaven
        
        History: delayed_update override no longer checks target.
        
        ==============================================================================
    """
        
    def delayed_update(self, frameDelta):
        super().delayed_update(frameDelta)
    
    """
        ==============================================================================
        
        Method: attack
        
        Description: Override attack, outputs whenever the player attacks an enemy.
        This method will have conditions detecting when it is possible for the player
        to attack it's target as given by the parameter enemy.
        
        Author: Jason Milhaven
        
        History: 
        
        ==============================================================================
    """
    
    def attack(self, enemy):
        print("attacking enemy")
        super().attack(enemy)
        
        