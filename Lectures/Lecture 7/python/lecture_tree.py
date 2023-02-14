
# Node representerar ett träd/subträd
class Node:
    def __init__(self, name: str):
        self.name = name  # Namn på fil / mapp
        self.children = []  # Länkar till noder

    def list_nodes(self, n: int = 0):
        """ Listar namnet på alla noder i trädet """
        indent = ' ' * n

        # Alla filer/mappar
        print(f"{indent}{self.name}")

        for child in self.children:
            child.list_nodes(n+2)

    def size(self):
        """ Antalet noder i träder/subträdet """
        s = 1  # Börja med 1

        # Lägg på 1 för varje barn
        for child in self.children:
            s += child.size()

        return s


if __name__ == '__main__':
    root_node = Node('lectures')
    n1 = Node('lecture 1')
    n2 = Node('lecture 2')
    n3 = Node('lecture 3')
    n4 = Node('linked_list.py')

    root_node.children = [n1, n2, n3]
    n2.children = [n4]

    print(root_node.size())
    print(n4.size())

    print()
    root_node.list_nodes()
