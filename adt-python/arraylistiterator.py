class ArrayListIterator(object):
	def __init__(self,backingStore):
		self._backingStore = backingStore
		self._modCount = backingStore.getModeCount()
		self.first()
	def first(self):
		"""resets the cursor to the beginning of the backing store"""
		self._cursor = 0
		self._lastItemPos=-1
	def hasNext(self):
		"""teturns true if the iterator has a next item"""
		return self._cursor<len(self._backingStore)
	def next(self):
		"""Preconditions:hasNext returns true.
		The list has not been modified except by this
		iterator's mutators.
		Returns the current item and advances the cursor to the next item"""
		if not self.hasNext():
			raise ValueError("no next item in list iterator")
		if self._modCount != self._backingStore.getModeCount():
			raise AttributeError("illegal modification of backing store")
		self._lastItemPos = self._cursor
		self._cursor+=1
		return self._backingStore[self._lastItemPos]
	def last(self):
		self._cursor = len(self._backingStore)
		self._lastItemPos=-1
	def hasPrevious(self):
		return self._cursor>0
	def previous(self):
		if not self.hasPrevious():
			raise ValueError("no previous item in list iterator")
		if self._modCount != self._backingStore.getModeCount():
			raise AttributeError("illegal modification of backing store")
		self._cursor -=1
		self._lastItemPos = self._cursor
		return self._backingStore[self._lastItemPos]
	#Mutator methods
	def replace(self,item):
		if self._lastItemPos == -1:
			raise AttributeError("the current position is undefined")
		if self._modCount != self._backingStore.getModeCount():
			raise AttributeError("list has been modified illegally")
		self._backingStore[self._lastItemPos] = item
		self._lastItemPos = -1
	def insert(self,item):
		if self._modCount != self._backingStore.getModeCount():
			raise AttributeError("list has been modified illegally")
		if self._lastItemPos ==-1:
			self._backingStore.add(item)
		else:
			self._backingStore.insert(self._lastItemPos,item)
		self._lastItemPos = -1
		self._modCount+=1
	def remove(self):
		if self._lastItemPos ==-1:
			raise AttributeError("the current position is undefined")
		if self._modCount != self._backingStore.getModeCount():
			raise AttributeError("list has been modified illegally")
		item = self._backingStore.pop(self._lastItemPos)
		#if the item removed was obtained via next,move cursor back 
		if self._lastItemPos < self._cursor:
			self._cursor -=1
		self._modCOunt +=1
		self._lastItemPos = -1
		