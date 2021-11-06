import numpy as np
import random
def detect_states(matrix):
    active, terminal = [], []
    for rowN, row in enumerate(matrix):
        (active if sum(row) else terminal).append(rowN)
    return(active,terminal)
def simplest_form(B):
    B = B.round().astype(int).A1
    gcd = np.gcd.reduce(B)
    B = np.append(B, B.sum())
    return (B / gcd).astype(int)
def solution(m):
    active, terminal = detect_states(m)
    if 0 in terminal:
        return [1] + [0]*len(terminal[1:]) + [1]
    m = np.matrix(m, dtype=float)[active, :]
    comm_denom = np.prod(m.sum(1))
    P = m / m.sum(1)
    Q, R = P[:, active], P[:, terminal]
    I = np.identity(len(Q))
    N = (I - Q) ** (-1)
    B = N[0] * R * comm_denom / np.linalg.det(N)
    return simplest_form(B)

test = []
N = 5
MAX = 10
zero_prob = 0.2
absorb = 2

for i in range(N):
    row = []
    if i <= absorb:
        for j in range(N):
            if random.random() < zero_prob:
                row += [random.randint(0, 0)]
            else:
                row += [random.randint(0, MAX)]
    else:
        for j in range(N):
            row += [0]
    test += [row]
print(test.__repr__())
print(solution(test).tolist().__repr__())

