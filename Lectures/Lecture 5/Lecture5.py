
def linear_search(input_list, item):
    for index, value in enumerate(input_list):
        if value == item:
            return index

    return None


# unsorted_list = [4, 5, 1, 2, 15, 7]
# print(unsorted_list)
# print(linear_search(unsorted_list, 22))

def binary_search(input_list, item):
    first = 0
    last = len(input_list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if item == input_list[midpoint]:
            return midpoint  # Midpoint pekar på rätt index
        elif item < input_list[midpoint]:
            last = midpoint - 1  # Släng högersidan
        elif item > input_list[midpoint]:
            first = midpoint + 1  # Släng vänstersidan

    return None


# sorted_list = [1, 2, 7, 9, 12, 13, 17, 21, 22]
# sorted_list = [-14, -8, -7, 0, 2, 7, 21]
# print(binary_search(sorted_list, -11))

def bubble_sort(unsorted_list):
    lst = unsorted_list.copy()  # Vi vill inte ändra orginalet, utan skicka tillbaka en sorterad kopia

    compare_count = 0

    for i in range(0, len(lst) - 1):
        swapped = False
        for j in range(0, len(lst) - i - 1):
            compare_count += 1
            if lst[j] > lst[j+1]:
                # a, b = b, a
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break

    print("Compare count:", compare_count)
    return lst


print(bubble_sort([5, 4, 3, 2, 1, 0, -1]))
print(bubble_sort([8, 7, 1, 2, 3, 4, 5, 6]))

# 2 -> 1
# 3 -> 4
# 4 -> 9
# 5 -> 16
# 6 -> 25
# 7 -> 36
# (n - 1) * (n - 1)