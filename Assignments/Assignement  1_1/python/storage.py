
class Node:
    def __init__(self, data):
        """ Store the data, and set next to None"""
        self.data = data
        self.next = None

    def __str__(self):
        """ Return a string representation of the data """
        return str(self.data)


class Storage:
    def __init__(self):
        """ Creates an empty Storage class. Sets head to None. """
        self.head = None

    def push(self, data):
        """ Create a Node to hold the data, then put it at the head of the list. """
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        """ Remove the head Node and return its data. """
        if self.head is not None:
            node = self.head
            self.head = self.head.next
            return node.data
        return None

    def peek(self):
        """ Return the data from the head Node, without removing it. """
        if self.head is not None:
            return self.head.data
        return None

    def isempty(self):
        """ Return True if the list is empty, otherwise False """
        if self.head is None:
            return True
        return False
    
    def swap(self, i, j):
        """ Swaps the nodes at index i and j """
        if i == j:
            return True
        
