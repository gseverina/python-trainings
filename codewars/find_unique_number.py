def find_uniq(arr):
    s = set(arr)
    for x in s:
        if arr.count(x) == 1:
            return x
    return 0


assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
assert find_uniq([ 3, 10, 3, 3, 3 ]) == 10
