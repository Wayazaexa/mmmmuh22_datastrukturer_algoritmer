from linked_list import Deque


def is_palindrome(word: str):
    # Är strängen "word" en palindrom

    dq = Deque()

    # Fylla vår deque med tecken
    for letter in word:
        dq.add_last(letter)

    while len(dq) > 1:
        # Ta första och sista tecknet från vår deque
        first = dq.remove_first()
        last = dq.remove_last()
        if first != last:
            return False

    return True


if __name__ == '__main__':
    print(is_palindrome('radar'))  # True
    print(is_palindrome('racecar'))  # True
    print(is_palindrome('tacocat'))  # True
    print(is_palindrome('palindrome'))  # False
