from linked_list import Deque

class Stack:
    def __init__(self):
        self.d = Deque()

    def push(self, item):
        self.d.add_first(item)

    def pop(self):
        return self.d.remove_first()
    
    def __len__(self):
        return self.d.size()
    
    def is_empty(self):
        return self.d.is_empty()
    
    def peek(self):
        return self.d.get_first()
    
class Queue:
    def __init__(self):
        self.d = Deque()

    def enqueue(self, item):
        self.d.add_last(item)
    
    def dequeue(self):
        return self.d.remove_first()
    
    def __len__(self):
        return self.d.size()
    
    def is_empty(self):
        return self.d.is_empty()
    
    def peek(self):
        return self.d.get_first()