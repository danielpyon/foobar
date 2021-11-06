def contains_cycle(s, size):
    n = len(s)
    prev = s[:size]
    for i in range(0, n, size):
        if s[i:i+size] != prev:
            return False
        prev = s[i:i+size]
    return True

def solution(s):
    n = len(s)
    for i in range(1, n):
        if n % i == 0:
            if contains_cycle(s, i):
                return n // i
    return 1
