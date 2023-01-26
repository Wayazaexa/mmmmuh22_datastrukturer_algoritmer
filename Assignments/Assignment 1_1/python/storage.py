
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
        if self.isempty():
            return False
        if i == j: # return true if i and j are the same
            return True
        if i < 0 or j < 0: # return false if i or j is out of bounds
            return False
        
        iPrev = self.head
        jPrev = self.head
        # To ensure I know which is the smaller index, I create new variables.
        ii = min(i, j)
        jj = max(i, j)
        
        if ii is 0:
            iCurr = self.head
            jj -= 1

            # Set jPrev to the node before index jj
            while jj > 0:
                jPrev = jPrev.next
                if jPrev.next is None:
                    return False
                jj -= 1
            jCurr = jPrev.next

            # Swap iCurr and jCurr
            tmp = jCurr.next
            if iCurr is jPrev: # Special case if iCurr and jCurr are adjacent
                jCurr.next = iCurr
            else:
                jCurr.next = iCurr.next
                jPrev.next = iCurr
            iCurr.next = tmp
            self.head = jCurr

            return True
        else:
            ii -= 1
            jj -= 1

            # Set iPrev to the node before index ii
            while ii > 0:
                iPrev = iPrev.next
                if iPrev.next is None: # Return false if ii is out of bounds
                    return False
                ii -= 1
                jPrev = jPrev.next
                jj -= 1
            iCurr = iPrev.next

            # Set jPrev to the node before index jj
            while jj > 0:
                jPrev = jPrev.next
                if jPrev.next is None: # Return false if jj is out of bounds
                    return False
                jj -= 1
            jCurr = jPrev.next

            # Swap iCurr and jCurr
            tmp = jCurr.next
            if iCurr is jPrev:
                jCurr.next = iCurr
            else:
                jCurr.next = iCurr.next
                jPrev.next = iCurr
            iCurr.next = tmp
            iPrev.next = jCurr

            return True
