from abstractcollection import AbstractCollection
class AbstractList(Abstractcollection):
	"""an abstract list implementation"""
	def __init__ (self,sourceCollection):
		"""maintains a count of modifications to the list"""
		self._modCount = 0 
		AbstractCollection.__init__(self,sourceCollection)
	def getModCount(self):
		"""returns the count of modifications to the list"""
		return self._modCount
	def incModCOunt(self):
		"""Increments the count of modifications to the list"""
		self._modCount += 1
	def index(self,item):
		"""Precondition:item is in the list.
		Returns the position of item
		Raises: ValueError if the item is not in the list"""
		position = 0
		for data in self:
			if data == item:
				return position
			else:
				position += 1
		if position == len(self):
			raise ValueError(str(item)+"not in list.")
	def add(self,item):
		"""adds the item to the end of the list."""
		self.insert(len(self),item)
	def remove(self,item):
		"""Precondition:item is in self
		Raises:ValueError if item is not in self
		Postcondition: item is removed from self."""
		position = self.index(item)
		self.pop(position)