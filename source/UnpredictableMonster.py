
import random

from Monster import *

"""
    ******************************************************************************

    Class: UnpredictableMonster
    
    Description: Moves randomly within constraints.
    
    Author: Jason Milhaven
    
    History:
    
    ******************************************************************************
"""

class UnpredictableMonster(Monster):

    """
        ==============================================================================
        
        Method: init
        
        Description: Defines a min and max offset which is to be randomly generated.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """

    def __init__(self, posX = 0, posY = 0, room = None):
        super().__init__(posX, posY, room)
        
        self.offsets = [
            (0, 0)
        ]
        self.offsetMin = -100
        self.offsetMax = 100
    
    """
        ==============================================================================
        
        Method: init
        
        Description: Override _on_offset_completed_, when self finishes it's offset,
        a new offset is randomly generated given the min and max offset values.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """

    # there is only one offset at a given time, so completedIndex == newIndex
    def _on_offset_completed_(self, completedIndex, newIndex, totalOffsetsCompleted):
        self.offsets[completedIndex] = (random.randrange(self.offsetMin, self.offsetMax), random.randrange(self.offsetMin, self.offsetMax))
        #print(self.offsets[self.__currentOffset__])
        