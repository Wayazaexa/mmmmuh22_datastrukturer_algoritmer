# sum(10) = 10+9+8+7+6+5+4+3+2+1  +0
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)

def tail_sum(mysum, n):
    if n==0:
        return mysum
    else:
        return tail_sum(mysum+n, n-1)
    

#print(tail_sum(0,-1))
print(sum(0))
print(sum(10))
print(tail_sum(0,10))