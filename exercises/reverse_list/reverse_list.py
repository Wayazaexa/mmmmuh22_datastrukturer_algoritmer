def reverse_list_basic(list):
    if list == []:
        return list
    else:
        first = list.pop(0)
        return reverse_list(list) + [first]

def reverse_list_back_to_front(list):
    if list == []:
        return list
    else:
        return list[-1:] + reverse_list(list[:-1])

def reverse_list(list):
    if list == []:
        return list
    else:
        return reverse_list(list[1:]) + [list[0]]

if __name__=='__main__':
    print(reverse_list([]))
    print(reverse_list([1]))
    print(reverse_list([1, 2]))
    print(reverse_list([1, 2, 3, 4, 5]))