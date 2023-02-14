import math
import sys
import time
import threading

#          a  b
# 0, 1, 1, 2, 3, 5, 8
# Vilket index har första talet med 1000 siffror

def fib_iter():
    a = 0
    b = 1
    index = 1
    while int(math.log10(b))+1 != 200:
        a, b = b, a+b
        index += 1
    
    return index
    

def fib(a=0, b=1, index=1):
    # if len(str(b)) == 1000:
    #     return index
    if int(math.log10(b))+1 == 200:
        return index
    
    return fib(b, a+b, index+1)


if __name__ == '__main__':
    print("__Iteration__")
    tic = time.perf_counter()
    answer = fib_iter()
    toc = time.perf_counter()
    print("Index:", answer)
    print("Time:", toc - tic)

    print("__Recursion__")
    sys.setrecursionlimit(5000)
    
    tic = time.perf_counter()
    answer = fib()
    toc = time.perf_counter()
    print("Index:", answer)
    print("Time:", toc - tic)


