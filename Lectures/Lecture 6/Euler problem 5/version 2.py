import time

# Euler 5
# MGN för 1-10 är 2520
# Vad är MGN för 1-20?

# Försök 1 - 21 sekunder
# Försök 2 - 20 sekunder


def calc_smallest_multiple(step):
    found = False
    ans = step
    
    while not found:
        ans += step
        # Gör om for-loopen till en list comprehension istället
        found = all([ans % n == 0 for n in range(1, 21)])

    return ans


if __name__ == '__main__':
    tic = time.perf_counter()  # Starta en timer
    answer = calc_smallest_multiple(20)
    toc = time.perf_counter()  # Stoppa timern

    print("Answer:", answer)
    print("Time:", toc-tic)
