import time

# Euler 5
# MGN för 1-10 är 2520
# Vad är MGN för 1-20?

# Försök 1 - 21 sekunder
# Försök 2 - 20 sekunder
# Försök 3 - 8 sekunder
# Försök 4 - 7 sekunder


def calc_smallest_multiple(step):
    check_nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # Byt ut while-loopen mot en for-loop och gör en return i loopen
    for ans in range(step, 999999999, step):
        if all(ans % n == 0 for n in check_nums):
            return ans


if __name__ == '__main__':
    tic = time.perf_counter()  # Starta en timer
    answer = calc_smallest_multiple(20)
    toc = time.perf_counter()  # Stoppa timern

    print("Answer:", answer)
    print("Time:", toc-tic)
