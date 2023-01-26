from linked_list import LinkedList


class Queue(LinkedList):
    def enqueue(self, item):
        """ Add item to start of the linked list """
        self.prepend(item)

    def dequeue(self):
        """ Remove and return item from end of the linked list """
        data = self.tail.data
        self.remove_last_node()
        return data

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.tail is None:
            return None

        return self.tail.data

    def size(self):
        pass


if __name__ == '__main__':
    my_queue = Queue()
    print("my_queue:", my_queue)

    print("Empty?", my_queue.is_empty())
    print()

    my_queue.enqueue("hello")
    print("my_queue:", my_queue)

    my_queue.enqueue("world")
    print("my_queue:", my_queue)

    print("Empty?", my_queue.is_empty())
    print("peek:", my_queue.peek())
    print()

    print("dequeue:", my_queue.dequeue())
    print("my_queue:", my_queue)
    print("dequeue:", my_queue.dequeue())
    print("my_queue:", my_queue)

    print("peek:", my_queue.peek())
