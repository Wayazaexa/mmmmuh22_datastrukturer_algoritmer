
# Detta är en lösning (en naiv lösning) av uppvärmningsproblemet. 
# Summera multipler av 3 och 5
# Se min Jupiter fil (SumProblem.ipynb) för en lösning med bättre komplexitet, inklusive förklaring

# Från 0 till 1000:
# Om jämt delbart med 3 eller 5: Summera
# Komplexitet: O(n)
# Bevis: Antal operationer: n-loopar. Antal operationer per loop: 3?
# 3*n -> O(n)
def even_3_5_sum(limit):
    s = 0

    for number in range (0, limit):
        # Om number är delbart med 3 eller 5, addera det till s
        if number % 3 == 0 or number % 5 == 0:
            s += number

    return s

def even_sum_gauss(div, limit):
    m = (limit - 1) / div
    return m * (m + 1) / 2 * div

def even_3_5_sum_gauss(limit):
    return even_sum_gauss(limit, 3) + even_sum_gauss(limit, 5) - even_sum_gauss(limit, 15);

if __name__ == '__main__':
    print(even_3_5_sum(10))  # Ska bli 23
    print(even_3_5_sum(1000))
    print(even_3_5_sum(10000))

    print("More efficient:")
    print(even_3_5_sum_gauss(1000))
    print(even_3_5_sum_gauss(10000))
    