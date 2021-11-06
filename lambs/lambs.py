import math

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def fib_sum(n):
    sum = 0
    i = 0
    f = fib()
    while sum <= n:
        sum += next(f)
        i += 1
    return i - 1

def solution(total_lambs):
    if total_lambs == 1:
        return 1

    # max: 1 + 1 + 2 + 3 ... <= total_lambs
    # min: 1 + 2 + 4 + 8 ... <= total_lambs
    max = fib_sum(total_lambs)
    min = int(math.floor(math.log(total_lambs + 1, 2)))

    return max - min

print(solution(10))
print(solution(143))
print(solution(100))
print(fib_sum(10))
