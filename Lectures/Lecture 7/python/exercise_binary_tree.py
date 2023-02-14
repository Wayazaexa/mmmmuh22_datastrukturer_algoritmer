
# Node beskriver ett binärt träd
class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

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


if __name__ == '__main__':
    root_node = Node('uggla')
    n1 = Node('hamster')
    n2 = Node('apa')
    n3 = Node('gorilla')
    n4 = Node('häst')
    n5 = Node('lemur')
    n6 = Node('pingvin')
    n7 = Node('varg')

    root_node.left = n1
    root_node.right = n6
    n1.left = n2
    n1.right = n4
    n2.right = n3
    n4.right = n5
    n6.right = n7

    print(root_node.size())
    print(n6.size())
    print(n7.size())

    print()
    print(root_node.height())

    print()
    print(n7.level(root_node))
    print(n3.level(n5))
