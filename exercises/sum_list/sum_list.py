def sum_list(list):
    if list == []:
        return 0
    else:
        return list.pop() + sum_list(list)

if __name__=='__main__':
    print(sum_list([]))
    print(sum_list([2, 4, 6]))