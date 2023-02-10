def bubblesort(list): # Bubble up
    count = 0
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            count += 1
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    print("Count 1: ", count)

def bubblesort_2(list):
    count = 0
    for i in range(len(list) - 1):
        swapped = False
        for j in range(len(list) - i - 1):
            count += 1
            if list[j] > list[j + 1]:
                swapped = True
                list[j], list[j + 1] = list[j + 1], list[j]
        if not swapped:
            break
    print("Count 2: ", count)

if __name__ == '__main__':
    lista = [5, 3, 7, 0, 6, 2, 1, 4, 8, 9]
    print(lista)
    bubblesort(lista)
    print(lista)
    lista = [5, 3, 7, 0, 6, 2, 1, 4, 8, 9]
    bubblesort_2(lista)
    print(lista)
