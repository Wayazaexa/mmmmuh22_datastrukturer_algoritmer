

# Räkna ut 100!, summera siffrorna i svaret

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def sum_digits(n):
    # För nummret n, summera siffrorna
    # Gör till en sträng
    # 933262 -> "966262"
    """
    s = 0
    for digit in str(n):
        # Summera siffrorna
        s += int(digit)

    return s
    """

    if n < 10:
        return n

    return n % 10 + sum_digits(n // 10)


f = factorial(100)
print('factorial: ' + str(f))
print('Sum of digits: ' + str(sum_digits(f)))
