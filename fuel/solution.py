import math

def log(n, b):
    return int(round(math.log(n, b)))

def closest_power(n, b):
    return b ** log(n, b)

def power_diff(n, b=2):
    # difference between n and nearest power of b
    return int(abs(n - closest_power(n, b)))

def solution(n):
    n = int(n)
    i = 0
    while n != 1:
        if power_diff(n) == 0:
            return i + log(n, 2)
        if n % 2 == 0:
            n //= 2
            i += 1
        else:
            if power_diff((n - 1) // 2) < power_diff((n + 1) // 2):
                n -= 1
            else:
                n += 1
            n //= 2
            i += 2
    return i

import sys
try:
    print(solution(sys.argv[1]))
except:
    assert solution('15') == 5
    assert solution('4') == 2

