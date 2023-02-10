
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0  # Håller koll på listans längd. Måste uppdateras om vi lägger till och tar bort noder.

    def __str__(self):
        """ __str__ Gör en sträng av vår instans: str(my_list) """
        node = self.head
        my_str = ""

        while node is not None:
            # För varje nod i listan, lägg på värdet och en pil
            my_str += f"{node.data} -> "
            node = node.next

        my_str += "None"  # Avsluta med "None"
        return my_str

    def __iter__(self):
        """ __iter__ låter oss använda for-loopar: for item in my_list """
        current = self.head

        while current is not None:
            yield current.data  # Yield ger tilbaka värdet, och pausar
            current = current.next

    def __contains__(self, data):
        """ __contains__ låter oss använda 'value in my_list' precis som andra listor """
        current = self.head

        while current is not None:
            # Gå igenom listan nod för nod
            if current.data == data:
                # Har vi hittat datan?
                return True

            current = current.next

        # Har vi kommit ned hit så fanns inte datan i listan
        return False

    def __len__(self):
        """ __len__ låter oss använda len(my_list) """
        return self._size

    def get_first_item(self):
        return self.head.data

    def get_last_item(self):
        return self.tail.data

    def count(self):
        """ Count the number of nodes in the list. """
        len(self)  # Anropa len() på listan

    def sum(self):
        """ Return the sum of all data in the list. Assumes data is addable (a + b). """
        node = self.head
        s = 0

        while node is not None:
            s += node.data
            node = node.next

        return s

    def append(self, data):
        """ Add the data to a node at the end of the list """

        new_node = Node(data)  # Create a new node

        if self.head is None or self.tail is None:
            # List was empty
            self.head = new_node
            self.tail = new_node
        else:
            # List is not empty, just add the node to the end
            self.tail.next = new_node  # Add new node after the last node (the tail)
            self.tail = new_node  # Move "tail" pointer to our new node

        self._size += 1

    def prepend(self, data):
        """ Add the data to a node at the start of the list """
        # 1. Skapa en ny nod
        new_node = Node(data)

        # 2. Sätt den nya nodens "next" till self.head
        new_node.next = self.head

        # 3. Flytta self.head till den nya noden
        self.head = new_node

        # 4. Om listan är tom: Uppdatera tail
        if self.tail is None:
            self.tail = new_node

        self._size += 1

    def insert(self, data, after_data):
        """ Insert data in a new node, placed after the node containing 'after_data' """
        # 1. Skapa en ny nod
        new_node = Node(data)

        # Är listan tom?
        if self.head is None:
            raise IndexError("can't insert into an empty list")

        # 2. Hitta rätt ställe i listan
        current = self.head
        while current.data != after_data:
            current = current.next
            if current is None:
                raise IndexError(f"{after_data=} not found in list")

        # 3. Sätt den nya nodens "next" till nästa nod
        new_node.next = current.next
        # 4. Sätt nuvarande nodens "next" till nya noden
        current.next = new_node

        self._size += 1

    def remove_first_node(self):
        """ Remove the first node from the list """

        # (1. Om listan är tom: Ge IndexError)
        if self.head is None:
            raise IndexError("list is empty")

        data = self.head.data  # Spara värdet innan noden tas bort

        # Flytta "self.head" till nästa nod
        self.head = self.head.next

        # Om vi precis tog bort sista elementet så ska vi uppdatera tail också
        if self.head is None:
            self.tail = None

        self._size -= 1
        return data

    def remove_last_node(self):
        """ Remove the last node from the list """

        # (1. Om listan är tom: Ge IndexError)
        if self.head is None:
            raise IndexError("list is empty")

        # 2. Skapa två tillfälliga pekare "current" och "previous"
        current = self.head
        temp_previous = self.head

        # Lagra värdet i sista noden innan den tas bort
        data = None

        # 3. Stega tills "current" är sista noden (current.next är None)
        while current is not None:
            if current.next is None:
                data = current.data  # Sista noden. Spara värdet.

                if current == self.head:
                    # Sista och första noden var samma. Dvs listan hade bara en nod. Töm listan.
                    self.head = None
                    self.tail = None
                else:
                    # 4. Sätt previous.next = None
                    temp_previous.next = None
                    self.tail = temp_previous

            temp_previous = current
            current = current.next

        self._size -= 1
        return data

    def remove_node(self, data):
        """ Remove the node containing 'data' """

        if self.head is None:
            raise IndexError("list is empty")

        # Börja med att stega från listans start
        current = self.head
        previous = self.head

        while current is not None:
            # Om detta är noden vi letar efter...
            if current.data == data:
                # Om vi är i starten av listan
                if current == self.head:
                    # Flytta head ett steg åt höger
                    self.head = current.next
                else:
                    # Vi är inte i starten av listan: Flytta förra elementets next ett steg åt höger
                    previous.next = current.next

                # Tog vi bort det sista elementet?
                if self.head is None:
                    self.tail = None
                elif current == self.tail:
                    # Flytta tail ett steg åt vänster
                    self.tail = previous

                # Vi har tagit bort första matchande noden. Avsluta metoden.
                self._size -= 1
                return

            # Vi har inte hittat det vi var ute efter: Flytta båda pekarna
            previous = current
            current = current.next


class Deque(LinkedList):
    # Övn. 1: Implementera en Deque-klass

    def add_first(self, item):
        """ Lägg till 'item' först i listan """
        self.prepend(item)

    def add_last(self, item):
        """ Lägg till 'item' sist i listan """
        self.append(item)

    def remove_first(self):
        """ Remove first item in the list and return the value """
        return self.remove_first_node()

    def remove_last(self):
        """ Remove the last item in the list and return the value"""
        return self.remove_last_node()

    def get_first(self):
        return self.get_first_item()

    def get_last(self):
        return self.get_last_item()

    def is_empty(self):
        return len(self) == 0

    def size(self):
        return len(self)


class Stack(Deque):
    # Övn. 2: Implementera en Stack och Kö ovanpå en Deque
    # Size, is_empty finns i Deque redan. Ingen mening med att implementera igen.

    def push(self, item):
        self.add_first(item)

    def pop(self):
        return self.remove_first()

    def peek(self):
        return self.get_first()


def deque_main():
    dq = Deque()
    print("Is empty?", dq.is_empty())
    print("Size?", dq.size())

    dq.add_first("a")
    dq.add_first("b")
    print(dq)
    print("Is empty?", dq.is_empty())

    dq.add_last("c")
    dq.add_last("d")
    print(dq)
    print("Is empty?", dq.is_empty())
    print("Size?", dq.size())

    print(dq.remove_first())
    print(dq.remove_first())
    # print(dq.remove_first())  # Ska ge ett fel
    print(dq)
    print("Is empty?", dq.is_empty())

    print(dq.remove_last())
    print(dq.remove_last())
    print(dq)
    print("Is empty?", dq.is_empty())
    print("Size?", dq.size())


def stack_main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print(s.size())
    print(s.is_empty())

    print("peek: ", s.peek())

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.is_empty())


if __name__ == '__main__':
    # Avkommentera för att köra testerna för deque resp. stack.
    # deque_main()
    # stack_main()
    pass
