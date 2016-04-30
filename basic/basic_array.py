import numpy as np

class Bag(object):
    
    '''
        Bag
        ---
        Implemented using numpy 1D array and array redoubeling
            add(item) - O(1) Amoritized
            is_empty - O(1)
            size - O(1)
    '''
    
    # dtype - type of the object stored in the bag
    def __init__(self, dtype='object'):
        self.N = 0
        self.items = np.empty(1, dtype=dtype)
        self.dtype = dtype
    
    def add(self, item):
        if self.N == len(self.items):
            self.__resize__(2 * self.N)
        self.items[self.N] = item
        self.N += 1
       
    @property    
    def is_empty(self):
        return self.N == 0
        
    @property
    def size(self):
        return self.N
    
    def __iter__(self):
        current = 0
        while current < self.size:
            yield self.items[current]
            current += 1
    
    def __resize__(self, new_size):
        print "resize %d" % new_size
        new_items = np.empty(new_size, dtype=self.dtype)
        for index in xrange(self.size):
            new_items[index] = self.items[index]
        self.items = new_items
             

class Stack(Bag):
    
    def __init__(self, dtype='object'):
        super(Stack, self).__init__(dtype=dtype)
    
    def push(self, item):
        self.add(item) 
        
    def pop(self):
        if self.N == 0:
            return None
        self.N -= 1
        item = self.items[self.N]
        if (3 * self.N <= len(self.items)):
            self.__resize__(len(self.items) / 2)
        return item
    
class Queue(object):
    
    def __init__(self, dtype='object'):
        self.end = 0
        self.start = 0
        self.N = 0
        self.items = np.empty(1, dtype='object')
        self.dtype = dtype
        
    def enqueue(self, item):
        if self.is_full:
            self.__resize__(2 * self.N)
        mod = len(self.items)
        self.items[self.end % mod] = item
        self.end = (self.end + 1) % mod
        self.N += 1
        
    def dequeue(self):
        if self.is_empty:
            return None
        mod = len(self.items)
        item = self.items[self.start]
        self.start = (self.start + 1) % mod
        self.N -= 1
        if (3 * self.N <= len(self.items)):
            self.__resize__(len(self.items) / 2)
        return item
        
    def __resize__(self, new_size):
        print "resize %d" % new_size
        new_items = np.empty(new_size, dtype=self.dtype)
        for i in xrange(self.N):
            new_items[i] = self.items[self.start]
            self.start = (self.start + 1) % len(self.items)
        self.start = 0
        self.end = i + 1
        self.items = new_items
        
    @property
    def size(self):
        return self.N
        
    @property
    def is_empty(self):
        return self.N == 0
        
    @property
    def is_full(self):
        return self.N == len(self.items)
           

            
        
