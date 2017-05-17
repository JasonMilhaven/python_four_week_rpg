
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

    def __init__(self, posX = 0, posY = 0, room = None):
        super().__init__(posX, posY, room)
        self.offsets = [
            (500, 0),
            (0, 500),
            (-500, 0),
            (0, -500),
            (250, 260),
            (-250, -260)
        ]
        self.moveSpeed = 100