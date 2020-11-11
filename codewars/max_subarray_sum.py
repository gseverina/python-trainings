def max_sequence(arr):
    i1 = 0
    i2 = i1 + 1
    end = len(arr)
    r = 0
    while i1 < end:
        sub = arr[i1:i2]
        s = sum(sub)
        if r < s:
            r = s

        if i2 == end:
            i1 += 1
            i2 = i1 + 1
        else:
            i2 += 1

    return r


assert max_sequence([]) == 0
assert max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
