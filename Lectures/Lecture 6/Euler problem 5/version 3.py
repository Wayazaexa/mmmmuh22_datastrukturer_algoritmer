import time

# Euler 5
# MGN för 1-10 är 2520
# Vad är MGN för 1-20?

# Försök 1 - 21 sekunder
# Försök 2 - 20 sekunder
# Försök 3 - 8 sekunder


def calc_smallest_multiple(step):
    found = False
    ans = step
    
    # 1. Gör om list-comprehensionens range(1, 21) till en vanlig lista.
    # 2. Ta bort alla tal som är faktorer av andra större tal i listan.
    #    Ex: 20: Alla tal som är jämt delbara med 20 är också jämt delbara med 1, 2, 4, 5, 10.
    #            Så ta bort 1, 2, 4, 5, 10 ur vår lista med tester
    #
    #    Gör vi det för alla tal så får vi listan 11-20.
    
    # check_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    check_nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    while not found:
        ans += step
        # Vi kan också göra om vår list-comprehension till en generator-comprehension
        # (Ta bort hak-parenteserna)
        found = all(ans % n == 0 for n in check_nums)
    
    return ans


if __name__ == '__main__':
    tic = time.perf_counter()  # Starta en timer
    answer = calc_smallest_multiple(20)
    toc = time.perf_counter()  # Stoppa timern

    print("Answer:", answer)
    print("Time:", toc-tic)
