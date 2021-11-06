from itertools import combinations

def solution(b, r):
    keys = [[] for _ in range(b)]
    # each key has b - (r - 1) copies
    # there are choose(b, r - 1) = choose(b, b - (r - 1)) unique keys
    # therefore, for each unique key, add it to the appropriate bunnies
    
    for i, buns in enumerate(combinations(range(b), b - (r - 1))):
        for bun in buns:
            keys[bun] += [i]

    return keys

#assert solution(3, 1) == [[0], [0], [0]]
#assert solution(2, 2) == [[0], [1]]
#assert solution(3, 2) == [[0, 1], [0, 2], [1, 2]]

print solution(5, 3)
