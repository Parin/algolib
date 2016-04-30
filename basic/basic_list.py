import numpy as np

class Stack(object):
    
    def __init__(self):
        self.top = None
        self.N = 0
        
    class Node(object):
        
        def __init__(self):
            self.key = None
            self.next = None
               
    def push(self, key):
        new_node = self.Node()
        new_node.key = key
        new_node.next = self.top
        self.top = new_node
        self.N += 1

    def pop(self):
        if self.is_empty:
            return None
        key = self.top.key
        self.top = self.top.next
        self.N -= 1
        return item
    
    @property
    def size(self):
        return self.N
        
    @property
    def is_empty(self):
        return self.N == 0
        
    def __iter__(self):
        current = self.top
        while current != None:
            yield current.key
            current = current.next

class Queue(object):
    
    def __init__(self):
        self.tail = None
        self.head = None
        self.N = 0
        
    class Node(object):
        
        def __init__(self):
            self.key = None
            self.next = None
            
    def enqueue(self, key):
        # save the pointer which is going to be changed by an operation
        # enqueue operation inserts at tail so save tail pointer 
        old_tail = self.tail
        # create new node and assign to tail pointer as we saved 
        # the old pointer already in previous step
        self.tail = self.Node()
        self.tail.key = key
        self.tail.next = None
        # check special case and update pointers
        if self.is_empty:
            self.head = self.tail
        else:
            old_tail.next = self.tail
        # done updating pointers so update count
        self.N += 1
        
    def dequeue(self):
        # before dequeueing check for empty
        if self.is_empty:
            return None
        # otherwise save the key
        key = self.head.key
        # move head to point to next node
        self.head = self.head.next
        # decrement the count
        self.N -= 1
        # adjust tail if list is empty now
        if self.is_empty:
            self.tail = self.head
        # return the key
        return key
        
        
    @property    
    def size(self):
        return self.N
    
    @property
    def is_empty(self):
        return self.N == 0
        
    def __iter__(self):
        current = self.head
        while current.next != None:
            yield current.key
            current = current.next



