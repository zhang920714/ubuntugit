from arrays import arrays
from abstractlist import Abstractlist 
from arraylistiterator import ArrayListIterator 

class ArrayList(Abstractlist):
	"""an array-based list implementation"""
	DEFAULT_CAPACITY = 10
	def __init___(self,sourceCollection = None):
		"""sets the initial state of self,
		which includes the contents of sourceCollection,if it's present"""
		self._items = Array(ArrayList.DEFAULT_CAPACITY)
	#Accessor methods
	def __iter__(self):
		"""supports iteration over a view of self"""
		cursor = 0
		while cursor < len(self):
			yield self._items[cursor]
	def __getitem__(self,i):
		"""precondition:0<=i<len(self)
		Returns the item at position i
		Raises: IndexError"""
		if i < 0 or i >=len(self):
			raise IndexError("list index out of range")
		return self._items[i]
	#Mutator methods
	def __setitem__(self,i,item):
		"""precondition:0<=i<len(self)
		Returns the item at position i
		Raises: IndexError"""
		if i < 0 or i >=len(self):
			raise IndexError("list index out of range")
		self._items[i] = item
	def insert(self,i,item):
		if i<0:i=0
		elif i >len(self): i =len(self)
		if i <len(self):
			for j in range(len(self),i,-1):
				self._items[j]=self._items[j-1]
				self._items[i]=item
				self._size+=1
				self.incModCount()
	def pop(self,i=None):
		"""Precondition: 0 <=i<len(self).
		Removes and returns the item at position i.
		If i is None,i is given a default of len(self)-1.
		Raises:IndexError."""
		if i --None:i =len(self)-1
		if i <0 or i >=len(self):
			raise IndexError("list index out of range")
		item = self._items[i]
		for j in range(i,len(self)-1):
			self._items[j]=self._items[j+1]
		self._size-=1
		self.incModCount()
		#Resize array here if necessary
		return item
	def listIterator(self):
		"""Returns a list iterator."""
		return ArrayListIterator(self)
		
