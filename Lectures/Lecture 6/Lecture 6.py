import random


# Fakultet (factorial)

def factorial(n):
    """ Räkna ut n-fakultet (n!) """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def sum_list(lst):
    """ Summera alla tal i en lista """
    # [5, 4, 2, 7, 1]
    # 5 + [4, 2, 7, 1]
    # 5 + 4 + [2, 7, 1]

    if len(lst) == 1:
        return lst[0]  # Basfall
    else:
        return lst[0] + sum_list(lst[1:])  # Rekursiva fallet


def power(n, p):
    """ Räkna ut n ^ p """
    if p == 0:  # basfall
        return 1
    else:  # Rekursivt fall
        return n * power(n, p-1)


def tail_factorial(product, num):
    """ Räkna ut n-fakultet (n!) """
    if num == 1:
        return product
    else:
        # Räkna ut multiplikation
        new_product = product * num
        return tail_factorial(new_product, num-1)


def infinite_recursions(nuke, count):
    if nuke == "Russia":
        return print("The world was saved by Koleshnikov")
    else:
        print(f"Nuke goes off in: {count}")
        if count == 1:
            if random.randint(1, 20) > 19:
                nuke = "Russia"
        return infinite_recursions(nuke, count-1)


def recurse(n):
    print(n)
    recurse(n+1)


if __name__ == '__main__':
    # recurse()
    # print(factorial(10))  # 10 * 9 * 8 * ... * 2 * 1
    # print(sum_list([5]))
    # print(sum_list([2, 5]))
    # print(sum_list([5, 4, 2, 7, 1]))
    # print(power(4, 3))  # 4 * 4 * 4

    # print(power(4, 0))  # == 1
    # print(power(4, 1))  # == 4  ( 4 * 1 )
    # print(power(4, 2))  # power(4, 2) * power(4, 1) * power(4, 0)
    # print(power(4, 6))  # 4096

    # print(tail_factorial(product=1, num=5))  # 120
    # infinite_recursions("Sweden", 995)

    import sys
    sys.setrecursionlimit(1500)
    print(sys.getrecursionlimit())
    recurse(1)
