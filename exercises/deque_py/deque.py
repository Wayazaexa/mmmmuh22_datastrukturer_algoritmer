"""
    add_first(x)   # Lägger till x på vänstra sidan av dequen
	add_last(x)    # Lägger till x på högra sidan av dequen
	remove_first() # Tar bort och ger tillbaka värdet längst till vänster
	remove_last()  # Tar bort och ger tillbaka värdet längst till höger

	is_empty()     # True om dequen är tom
	size()         # Ger antalet element i dequen
"""
class Deque:
    def __init__(self):
        self.list = []
    
    def add_first(self, x):
        self.list.insert(0, x)
    
    def add_last(self, x):
        self.list.append(x)
    
    def remove_first(self):
        if self.is_empty():
            return False
        else:
            return self.list.pop(0)
    
    def remove_last(self):
        if self.is_empty():
            return False
        else:
            return self.list.pop(len(self.list) - 1)
    
    def is_empty(self):
        return self.list == []

    def size(self):
        return len(self.list)

def is_palindrome(string):
    list = Deque()
    
    for char in string:
        list.add_first(char)
    
    while list.size() > 1:
        first = list.remove_first()
        last = list.remove_last()
        if not first == last:
            return False
    return True

if __name__ == '__main__':
    deque = Deque()
    deque.add_first(2)
    deque.add_first(1)
    deque.add_last(3)
    print(f"first: {deque.remove_first()}")
    print(f"last: {deque.remove_last()}")
    print(f"size: {deque.size()}")
    print(f"first: {deque.remove_first()}")
    print(f"empty? {deque.is_empty()}")
    print(f"is 'racecar' a palindrome? {is_palindrome('racecar')}")
    print(f"is 'palindrome' a palindrome? {is_palindrome('palindrome')}")
    print(f"is 'tacocat' a palindrome? {is_palindrome('tacocat')}")
