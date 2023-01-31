class Stack:
    def __init__(self):
        self.stack = []
        self._size = 0
    
    def push(self, x):
        self.stack.insert(0, x)
        self._size += 1
    
    def pop(self):
        self._size -= 1
        return self.stack.pop(0)
    
    def is_empty(self):
        return self._size == 0
    
    def peek(self):
        if self._size == 0:
            return ""
        else:
            return self.stack[0]
    
    def size(self):
        return self._size


if __name__ == '__main__':
    myStack = Stack()
    print(f"Empty? {myStack.is_empty()}")
    print("Pushing 3")
    myStack.push(3)
    print("Pushing 2")
    myStack.push(2)
    print("Pushing 1")
    myStack.push(1)
    print(f"Peeking: {myStack.peek()}")
    print(f"Size? {myStack.size()}")
    print(f"Popping: {myStack.pop()}")
    print(f"Popping: {myStack.pop()}")
    print(f"Empty? {myStack.is_empty()}")
    print(f"Size? {myStack.size()}")
    print(f"Popping: {myStack.pop()}")
    print(f"Empty? {myStack.is_empty()}")