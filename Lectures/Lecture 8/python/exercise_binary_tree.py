
# Node beskriver ett binärt träd
class Node:
    def __init__(self, key, name=''):
        self.key = key
        self.name = name
        self.left = None
        self.right = None

    # Print a tree with pre-order traversal
    def print_tree(self, n: int = 0):
        """ Listar namnet på alla noder i trädet """
        indent = ' ' * n

        print(f"{indent}{self.key} {self.name}")

        if self.left is not None:
            self.left.print_tree(n+2)
        if self.right is not None:
            self.right.print_tree(n+2)

    # Print a tree with mid-order traversal (binary search tree)
    def print_binary_tree(self):
        if self.left is not None:
            self.left.print_binary_tree()
        
        print(f"{self.key} {self.name}")

        if self.right is not None:
            self.right.print_binary_tree()

    def size(self):
        s = 1

        if self.left is not None:
            s += self.left.size()
        if self.right is not None:
            s += self.right.size()

        return s

    def height(self, height=1):
        # Valfritt: Explicit basfall. Hanteras av koden nedanför om vi skippar detta.
        if self.left is None and self.right is None:
            return height

        # Vilken höjd får vi tillbaka från våra barn
        left_height = height
        right_height = height

        if self.left is not None:
            left_height = self.left.height(height + 1)
        if self.right is not None:
            right_height = self.right.height(height + 1)

        # Vilken av höjderna är störst
        return max(left_height, right_height)

    def level(self, root, distance=0):
        # Self är vår nod nere i träder och root är noden vi vill jämföra med.
        # Rekursera och gå vänster/höger genom att byta ut root.
        # DVS: Vi börjar på en nod och vandrar runt tills vi hittar "self"-noden

        # Har vi hittat rätt nod?
        if self == root:
            return distance

        if root.left is not None:
            # Rekursivt anrop åt vänster om det finns något där
            left_level = self.level(root.left, distance + 1)
            if left_level is not None:
                # Om sökningen lyckades, vi hittade self-noden genom att gå åt vänster
                return left_level

        if root.right is not None:
            # Rekursivt anrop åt höger om det finns något där
            right_level = self.level(root.right, distance + 1)
            if right_level is not None:
                # Om sökningen lyckades, vi hittade self-noden genom att gå åt höger
                return right_level

        # Om noden vi besöker inte är self-noden vi letar efter,
        # men vi inte kan gå åt något håll (vänster eller höger),
        # så måste vi indikera att vi misslyckades. Därför skickar
        # vi tillbaka "None"
        return None
    
    def is_balanced(self):
        """ Returnerar om trädet är balanserat """
        # Använder hjälpfunktion för rekursion, som returnerar både höjd och om det är balanserat
        bal, height = self.is_balanced_with_height()
        return bal

    def is_balanced_with_height(self, height=1):
        """Hjälpfunktion. Returnerar både om trädet är balanserat och dess höjd"""

        left_height = height
        right_height = height
        left_bal = True
        right_bal = True
        if self.left is not None:
            left_bal, left_height = self.left.is_balanced_with_height(height + 1)
        if self.right is not None:
            right_bal, right_height = self.right.is_balanced_with_height(height + 1)
        
        bal = left_bal and right_bal and (abs(left_height - right_height)<=1)
        # Debug printing
        #if not bal:
        #    print(f"Tree starting with node {self.key} is not balanced. left_bal: {left_bal}, right_bal: {right_bal}, left_height: {left_height}, right_height: {right_height}")
        #else :
        #    print(f"Tree starting with node {self.key} is balanced. left_bal: {left_bal}, right_bal: {right_bal}, left_height: {left_height}, right_height: {right_height}")

        return bal, max(left_height, right_height)
    
    def is_binary_order(self):
        return self.is_binary_order_with_min_max(None, None)
    
    def is_binary_order_with_min_max(self, min, max):
        if min is not None and self.key <= min:
            # Debug printing
            #print(f"Node: {self.key}. Not smaller. Min? {min}. Max? {max}")
            return False
        if max is not None and self.key >= max:
            # Debug printing
            #print(f"Node: {self.key}. Not larger. Min? {min}. Max? {max}")
            return False
        
        l_bin = True
        r_bin = True
        if self.left is not None:
            l_bin = self.left.is_binary_order_with_min_max(min, self.key)
        if self.right is not None:
            r_bin = self.right.is_binary_order_with_min_max(self.key, max)
        
        bin = l_bin and r_bin

        # Debug printing
        #print(f"Node: {self.key}. Is binary? {bin}. Left? {l_bin}. Right? {r_bin}. Min? {min}. Max? {max}")
        
        return l_bin and r_bin
    
    def search(self, value):
        """ Searching assuming in binary order"""
        if self.key == value:
            return self

        if self.left is not None and value < self.key:
            return self.left.search(value)
        if self.right is not None and value > self.key:
            return self.right.search(value)
        
        # Hittades inte
        return None
    
    def insert(self, n):
        
        if n.key < self.key:
            if self.left is None:
                self.left = n
            else:
                self.left.insert(n)
        elif n.key > self.key:
            if self.right is None:
                self.right = n
            else:
                self.right.insert(n)
        else:
            raise Exception("Equal keys not supported")

        

if __name__ == '__main__':
    ## Unbalanced tree (still binary)
    root_node = Node(8)
    # I call the nodes after the number they hold, easier to create the tree and don't mix up later
    n3 = Node(3)
    n1 = Node(1)
    n6 = Node(6)
    n4 = Node(4)
    n7 = Node(7)
    n10 = Node(10)
    n14 = Node(14)
    n13 = Node(13)

    root_node.left = n3
    root_node.right = n10
    n3.left = n1
    n3.right = n6
    n6.left = n4
    n6.right = n7
    n10.right = n14
    n14.left = n13

    print("Tree printed:")
    root_node.print_tree()

    print()
    print("Tree printed in order:")
    root_node.print_binary_tree()
    print()

    print(f"Is balanced? {root_node.is_balanced()}")
    print(f"Is binary order? {root_node.is_binary_order()}")

    ## Balanced tree. Not in binary order
    b_root_node = Node(3)
    # I call the nodes after the number they hold, easier to create the tree and don't mix up later
    b_n6 = Node(6)
    b_n7 = Node(7)
    b_n9 = Node(9)
    b_n10 = Node(10)
    b_n14 = Node(14)

    b_root_node.left = b_n7
    b_root_node.right = b_n10
    b_n7.left = b_n9
    b_n7.right = b_n6
    b_n10.right = b_n14

    print(f"Is b tree balanced? {b_root_node.is_balanced()}")
    print(f"Is b tree binary order? {b_root_node.is_binary_order()}")
    
    ## Balanced tree 2. Still not in binary order. (Each child is correctly in left<->right, but not whole tree)
    b2_root_node = Node(3)
    # I call the nodes after the number they hold, easier to create the tree and don't mix up later
    b2_n6 = Node(6)
    b2_n7 = Node(7)
    b2_n9 = Node(9)
    b2_n10 = Node(10)
    b2_n14 = Node(14)

    b2_root_node.left = b2_n7
    b2_root_node.right = b2_n10
    b2_n7.left = b2_n6
    b2_n7.right = b2_n9
    b2_n10.right = b2_n14

    print(f"Is b2 tree balanced? {b2_root_node.is_balanced()}")
    print(f"Is b2 tree binary order? {b2_root_node.is_binary_order()}")

    ## Balanced tree 3. In binary order. Now also adding a name
    b3_root_node = Node(9, 'häst')
    # I call the nodes after the number they hold, easier to create the tree and don't mix up later
    b3_n6 = Node(6, 'kanin')
    b3_n7 = Node(7, 'apa')
    b3_n3 = Node(3, 'marsvin')
    b3_n10 = Node(10, 'sköldpadda')
    b3_n14 = Node(14, 'blåsfisk')

    b3_root_node.left = b3_n6
    b3_root_node.right = b3_n10
    b3_n6.left = b3_n3
    b3_n6.right = b3_n7
    b3_n10.right = b3_n14

    print(f"Is b3 tree balanced? {b3_root_node.is_balanced()}")
    print(f"Is b3 tree binary order? {b3_root_node.is_binary_order()}")
    find_3 = b3_root_node.search(3)
    print(f"Nod 3: key: {find_3.key}, namn: {find_3.name}")
    find_15 = b3_root_node.search(15)
    print("Nod 15: ", find_15)
    print("Tree printed in order:")
    b3_root_node.print_binary_tree()
    print()    

    bin_root_node = Node(5, 'a')
    bin_n1 = Node(1, 'b')
    bin_n9 = Node(9, 'c')
    bin_n3 = Node(3, 'd')
    bin_n4 = Node(4, 'e')
    bin_n14 = Node(14, 'f')
    bin_n1_2 = Node(1, 'g')
    bin_root_node.insert(bin_n1)
    bin_root_node.insert(bin_n9)
    bin_root_node.insert(bin_n3)
    bin_root_node.insert(bin_n4)
    bin_root_node.insert(bin_n14)
    # bin_root_node.insert(bin_n1_2)  # Exception raised
    print(f"Is bin tree balanced? {bin_root_node.is_balanced()}")
    print(f"Is bin tree binary order? {bin_root_node.is_binary_order()}")
    print()
    print("Tree printed in order:")
    bin_root_node.print_binary_tree()
    print()    

    # print(root_node.size())
    # print(n6.size())
    # print(n7.size())

    # print()
    # print(root_node.height())

    # print()
    # print(n7.level(root_node))

