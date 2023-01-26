class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        value = self.stack[-1]
        del self.stack[-1]
        return value

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if len(self.stack) == 0:
            return None

        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    my_stack = Stack()
    print("my_stack:", my_stack)

    print("Empty?", my_stack.is_empty())

    print()

    my_stack.push("hello")
    print("my_stack:", my_stack)
    my_stack.push("world")
    print("my_stack:", my_stack)
    print("Empty?", my_stack.is_empty())

    print("peek:", my_stack.peek())
    print()

    print("pop:", my_stack.pop())
    print("my_stack:", my_stack)
    print("pop:", my_stack.pop())
    print("my_stack:", my_stack)
    print("peek:", my_stack.peek())
