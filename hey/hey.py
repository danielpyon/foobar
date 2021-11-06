def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number, base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)

def get_id(n, b):
    k = len(n)
    arrange = lambda s, b, descending: int(''.join(sorted(list(s), reverse=descending)), base=b)
    while True:
        x, y = arrange(n, b, True), arrange(n, b, False)
        z = str_base(x - y, b).zfill(k)
        yield z
        n = z

def solution(n, b):
    # make a generator (n, b)
    # use set to keep track of seen
    # next(gen) while next(gen) is not in seen
    # once you see, start the counter until the next one (guaranteed to find the same cycle since the algo is deterministic)
    
    ids = get_id(n, b)
    seen = set()
    count = False
    cycle_length = 0
    start = None
    while True:
        if count:
            cycle_length += 1
        id = next(ids)
        if id == start:
            return cycle_length
        elif id in seen and not count:
            start = id
            count = True
        else:
            seen.add(id)

print(solution('1211', 10))
print(solution('210022', 3))
