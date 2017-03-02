
class Transform():

	def __init__(self, posX = 0, posY = 0, sizeX = 0, sizeY = 0):
		if type(self) == Transform:
			raise TypeError("do not instantiate a Transform directly")
		self.name = ""
		self._posX_ = posX
		self._posY_ = posY
		self._sizeX_ = sizeX
		self._sizeY_ = sizeY
	
	# single field accessors
	
	def get_pos_x(self):
		return self._posX_
	
	def set_pos_x(self, v):
		self._posX_ = v
		
	def get_pos_y(self):
		return self._posY_
		
	def set_pos_y(self, v):
		self._posY_ = v
	
	def get_size_x(self):
		return self._sizeX_
	
	def set_size_x(self, v):
		self._sizeX_ = v
		
	def get_size_y(self):
		return self._sizeY_
		
	def set_size_y(self, v):
		self._sizeY_ = v
	
	# multiple field accessors
	
	def get_pos(self):
		return (get_pos_x(), get_pos_y())
	
	def set_pos(self, x, y):
		self.set_pos_x(x)
		self.set_pos_y(y)
	
	def get_size(self):
		return (get_size_x(), get_size_y())
	
	def set_size(self, x, y):
		self.set_size_x(x)
		self.set_size_y(y)
	