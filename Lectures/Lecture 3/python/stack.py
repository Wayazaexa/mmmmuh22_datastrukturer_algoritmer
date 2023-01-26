from linked_list import LinkedList


class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, item):
        """ Add item to start of the linked list """
        self.prepend(item)

    def pop(self):
        """ Retrieve item from start of linked list, and remove it """
        data = self.head.data
        self.remove_first_node()
        return data

    def is_empty(self):
        # return self.head is None
        return len(self) == 0

    def peek(self):
        if self.head is None:
            return None

        return self.head.data

    def size(self):
        return len(self)


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
