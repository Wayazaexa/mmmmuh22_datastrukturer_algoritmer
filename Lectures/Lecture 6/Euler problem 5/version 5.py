import time

# Euler 5
# MGN för 1-10 är 2520
# Vad är MGN för 1-20?

# Försök 1 - 21 sekunder
# Försök 2 - 20 sekunder
# Försök 3 - 8 sekunder
# Försök 4 - 7 sekunder
# Försök 5 - 0.06 sekunder


def calc_smallest_multiple(step):
    check_nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for ans in range(step, 999999999, step):
        if all(ans % n == 0 for n in check_nums):
            return ans


# Från uppgiften får vi att det minsta talet som är jämt delbart med 1-10 är 2520.
# Så byt ut vårat steg 20 mot 2520.
if __name__ == '__main__':
    tic = time.perf_counter()  # Starta en timer
    answer = calc_smallest_multiple(2520)  # Byt ut 20 mot 2520. 
    toc = time.perf_counter()  # Stoppa timern

    print("Answer:", answer)
    print("Time:", toc-tic)
