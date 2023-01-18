
if __name__ == '__main__':

    # Listor
    my_list = [1, 2, 3, 4, 5, 6]
    print(my_list[0])
    print(my_list[5])
    print(my_list[-1])

    # Dictionaries
    my_dict = {}  # dict()
    my_dict2 = {
        'name': 'David',
        'age': 37,
        'cats': ['Apollo', 'Luna']
    }
    print(my_dict2.get('age'))
    print(my_dict2.get('cats'))

    # Classes
    class MyClass:
        def __init__(self, value):
            self.value = value

        def print_value(self):
            print(self.value)

    c = MyClass(99)
    c.print_value()
