from math import floor, sqrt
from decimal import *

def S(n):
    n = int(n)
    m = int(floor((sqrt(2) - 1) * n))
    c = lambda n, m: n * m + n * (n + 1) // 2 - m * (m + 1) // 2
    
    if n == 0:
        return 0
    
    return c(n, m) - S(m)

getcontext().prec = 10000
SQRT2 = Decimal(2).sqrt()
def s(n):
    m = int(Decimal(n) * (SQRT2 - Decimal(1)) // 1)
    c = lambda n, m: n * m + n * (n + 1) // 2 - m * (m + 1) // 2

    if n == 0:
        return 0

    return c(n, m) - s(m)

def solution(str_n):
    return str(s(int(str_n)))

print solution('5')
print solution('77')
print solution(10**100)

print s(10**100)
