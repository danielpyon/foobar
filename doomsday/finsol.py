import numpy as np
from fractions import Fraction, gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def common_denominator(fracs):
    # Given a list of fractions, returns a list of numerators with the last element being the common denominator
    denominator = reduce(lcm, map(lambda x: x.denominator, fracs))
    numerators = list(map(lambda x: x.numerator * denominator // x.denominator, fracs))
    return numerators + [denominator]

def solution(m):
    non_absorbing_states, absorbing_states = [], []
    for i, row in enumerate(m):
        if sum(row) == 0:
            absorbing_states.append(i)
        else:
            non_absorbing_states.append(i)

    if 0 in absorbing_states:
        # All absorbing states, since index 0 is absorbing
        return [1] + [0] * (len(m) - 1) + [1]

    P = np.matrix(m, dtype=float)[non_absorbing_states, :]
    
    # Probabilities
    P = P / P.sum(1)
    Q = P[:, non_absorbing_states]
    R = P[:, absorbing_states]
    I = np.eye(len(Q))
    F = np.linalg.inv(I - Q)
    
    fractionize = np.vectorize(lambda x: Fraction(x).limit_denominator())
    ans = fractionize(F[0] * R).tolist()[0]

    return common_denominator(ans)

print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
