import time

# Euler 5
# MGN för 1-10 är 2520
# Vad är MGN för 1-20?

# Försök 1 - 21 sekunder


def calc_smallest_multiple(step):
    found = False  # Fortsätt tills "found"-flaggan är True
    ans = step  # Börja testa på 20

    while not found:
        ans += step  # Alla tal ska vara jämt delbara med 20, så stega med 20
        ans_list = []
        
        for n in range(1, 21):
            # Testa om 1-20 är jämt delbart med vår tal
            # Bygg en lista med True/False
            ans_list.append(ans % n == 0)
            
        found = all(ans_list)  # Avbryt loopen om alla värden i listan var True
    
    return ans


if __name__ == '__main__':
    tic = time.perf_counter()  # Starta en timer
    answer = calc_smallest_multiple(20)
    toc = time.perf_counter()  # Stoppa timern

    print("Answer:", answer)
    print("Time:", toc-tic)
