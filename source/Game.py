

from Player import *
from Room import *

class Game():

	def __init__(self, width, height):
		self.username = "?????"
		self.rooms = []
		self.player = Player()
		
		self.rooms.append(Room(width, height, self.player))
		self.currentRoom = self.rooms[0]