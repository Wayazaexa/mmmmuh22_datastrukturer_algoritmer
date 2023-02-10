def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

if __name__=='__main__':
    print(power(4, 0))
    print(power(4, 2))
    print(power(2, 8))