from fractions import Fraction, gcd
import math

def get_states(m):
    all_zero = lambda arr: all(map(lambda x: x == 0, arr))
    nonterm, term = [], []
    for i in range(len(m)):
        if sum(m[i]) == 0:
            term += [i]
        else:
            nonterm += [i]
    return nonterm, term

def sub(m, a, b):
    # submatrix
    m = m[a[0]:a[1]]
    ret = []
    for i in range(len(m)):
        c = []
        for j in range(len(m[0])):
            if j >= b[0] and j <= b[1]:
                c += [m[i][j]]
        ret += [c]
    return ret

def eye(n):
    ret = []
    for i in range(n):
        c = []
        for j in range(n):
            c += [Fraction(0, 1) if i != j else Fraction(1, 1)]
        ret += [c]
    return ret

def zeros(n):
    ret = []
    for i in range(n):
        c = []
        for j in range(n):
            c += [Fraction(0, 1)]
        ret += [c]
    return ret

def inv(m):
    def eliminate(r1, r2, col, target=0):
        fac = (r2[col]-target) / r1[col]
        for i in range(len(r2)):
            r2[i] -= fac * r1[i]

    def gauss(a):
        for i in range(len(a)):
            if a[i][i] == 0:
                for j in range(i+1, len(a)):
                    if a[i][j] != 0:
                        a[i], a[j] = a[j], a[i]
                        break
                else:
                    raise ValueError("Matrix is not invertible")
            for j in range(i+1, len(a)):
                eliminate(a[i], a[j], i)
        for i in range(len(a)-1, -1, -1):
            for j in range(i-1, -1, -1):
                eliminate(a[i], a[j], i)
        for i in range(len(a)):
            eliminate(a[i], a[i], i, target=1)
        return a

    tmp = [[] for _ in m]
    for i,row in enumerate(m):
        assert len(row) == len(m)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(m)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

def matsub(a, b):
    r, c = len(a), len(a[0])
    ret = []
    for i in range(r):
        x = []
        for j in range(c):
            x += [a[i][j] - b[i][j]]
        ret += [x]
    return ret

def matmul(a, b):
    ret = zeros(len(a))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                ret[i][j] += a[i][k] * b[k][j]
    return ret

def shape(m):
    return len(m), len(m[0])

def pad(m, n, down=True):
    r, c = shape(m)
    import copy
    ret = copy.deepcopy(m)
    if down:
        ret += [[Fraction(0, 1)] * c] * n
        return ret
    else:
        for row in ret:
            for x in range(n):
                row += [Fraction(0, 1)]
        return ret

def shiftright(m, n):
    r, c = shape(m)
    import copy
    ret = copy.deepcopy(m)
    for i in range(r):
        for x in range(n):
            ret[i] = [Fraction(0, 1)] + ret[i]
    return ret

def pprint(m):
    for i in m:
        s = ''
        for j in i:
            s += str(j).ljust(10) + ' '
        print(s)

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def select_rows(m, rows):
    ret = []
    for i in range(len(m)):
        if i in rows:
            ret += [m[i]]
    return ret

def remove_trailing_zeros(m):
    i = len(m) - 1
    while True:
        if m[i] != Fraction(0, 1):
            break
        i -= 1
    return m[:i + 1]

def solution(m):
    r, c = len(m), len(m[0])
    P = []

    for i in range(r):
        s = sum(m[i])
        curr = []
        for j in range(c):
            if m[i][j] == 0:
                curr += [Fraction(0, 1)]
            else:
                curr += [Fraction(m[i][j], s)]
        P += [curr]

    nonterm, term = get_states(P)
    if 0 in term:
        return [1] + [0] * len(term[1:]) + [1]

    Q = select_rows(P, nonterm)
    Q_dim, _ = shape(Q)
    Q = sub(P, (0, Q_dim), (0, Q_dim))
    R = sub(P, (0, Q_dim), (Q_dim, c - 1))
    I = eye(Q_dim)
    F = inv(matsub(I, Q))
    
    # F: 2x2 R: 2x4
    # matmul(F, R)

    largest_dim = max(*(shape(R) + shape(F)))
    R = pad(R, largest_dim - shape(R)[0], down=True)
    F = pad(F, largest_dim - shape(F)[1], down=False)
    F = pad(F, largest_dim - shape(F)[0], down=True)

    ans = matmul(F, R)[0]
    ans = remove_trailing_zeros(ans)
    
    denoms = []
    for frac in ans:
        denoms += [frac.denominator]
    common = reduce(lcm, denoms)
   
    final_ans = []
    for frac in ans:
        final_ans += [frac.numerator * (common // frac.denominator)]
    final_ans += [common]

    return final_ans


TEST = False

if not TEST:
    print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
    print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
    print(solution([[8, 2, 2, 9, 5], [3, 0, 4, 0, 1], [0, 2, 9, 1, 6], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
    print(solution([[3, 0, 0, 3, 0], [0, 2, 0, 1, 4], [10, 0, 10, 4, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))

if TEST:
    import sys
    data = eval(next(sys.stdin))
    ans = eval(next(sys.stdin))

    sol = solution(data)
    if sol != ans:
        print('Incorrect')
        print('Data: ' + str(data))
        print('Answer: ' + str(ans))
        print('What you got: ' + str(sol(data)))

