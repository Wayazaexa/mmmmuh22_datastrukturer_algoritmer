

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current_node = self.head
        my_str = ""

        while current_node is not None:
            my_str += f"{current_node.data} -> "
            current_node = current_node.next

        my_str += "None"
        return my_str
    
    def count(self):
        current_node = self.head
        sum = 0
        
        while current_node is not None:
            sum += 1
            current_node = current_node.next
        return sum

    def sum(self):
        current_node = self.head
        sum = 0

        while current_node is not None:
            sum += current_node.data
            current_node = current_node.next
        return sum

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            
            current.next = new_node


if __name__ == '__main__':
    llist = LinkedList()
    print(llist)

    #box1 = Node("a")
    #llist.head = box1
    llist.append(1)
    print(llist)

    #box2 = Node("b")
    #box1.next = box2
    llist.append(2)
    print(llist)

    #box3 = Node("c")
    #box2.next = box3
    llist.append(3)
    print(llist)

    size = llist.count()
    print(f"The list contains {size} nodes.")
    assert(size == 3)

    sum = llist.sum()
    print(f"The sum of the data in the list is {sum}.")
    assert (sum == 6)

    current_node = llist.head
    # Börja på första noden och gå till next, tills vi kommer till slutet
    while current_node is not None:
        # Skriva ut vad noden innehåller
        print(current_node.data)

        # Gå vidare till nästa nod
        current_node = current_node.next
