#!/usr/bin/python2

def solution(x, y):
    x, y = int(x), int(y)
    i = 0
    while True:
        if x == 1 and y == 1:
            break
        if x < 1 or y < 1:
            return 'impossible'
        if x == y:
            return 'impossible'
        if x == 1 or y == 1:
            i += max(x, y) - 1
            break
        if x > y:
            i += x // y
            x = x - (x // y) * y
        else:
            i += y // x
            y = y - (y // x) * x
    
    return str(i)

import sys
try:
    print(solution(*sys.argv[1:]))
except:
    assert solution('4', '7') == '4'
    assert solution('2', '1') == '1'
    assert solution('10', '4') == 'impossible'
    assert solution('1', '1') == '0'
    assert solution('2', '4') == 'impossible'
    assert solution('0', '1') == 'impossible'
