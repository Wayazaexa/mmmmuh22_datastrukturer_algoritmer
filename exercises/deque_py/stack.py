from deque import Deque

class Stack:
    def __init__(self):
        self.list = Deque()
    
    def push(self, x):
        self.list.add_first(x)
    
    def pop(self):
        return self.list.remove_first()
    
    def size(self):
        return self.list.size()
    
    def is_empty(self):
        return self.list.is_empty()
    
    def peek(self):
        return self.list[0]
