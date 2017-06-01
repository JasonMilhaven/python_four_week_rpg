
from Monster import *

"""
    ******************************************************************************

    Class: TestMonster
    
    Description: First Monster subclass used for testing, will likely be unused
    in the final game.
    
    Author: Jason Milhaven
    
    History:
    
    ******************************************************************************
"""

class TestMonster(Monster):

    """
        ==============================================================================
        
        Method: init
        
        Description: Vanilla constructor for TestMonster.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """

    def __init__(self, posX = 0, posY = 0, room = None):
        super().__init__(posX, posY, room)
        
        