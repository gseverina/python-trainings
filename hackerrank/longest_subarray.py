def longest_subarray(arr):
    r = []
    sub = []
    i1 = 0
    i2 = 0
    while i2 < len(arr):
        x = arr[i2]
        if sub.count(x) < 2:
            sub.append(x)
            if len(set(sub)) > 2:
                sub.pop()
                if len(sub) > len(r):
                    r = sub
                i1 += 1
                sub = arr[i1:i2+1]
            elif len(sub) == 4:
                i1 += 1
                if len(sub) > len(r):
                    r = sub
                elif len(sub) == len(r):
                    if sum(sub) > sum(r):
                        r = sub
                sub = arr[i1:i2+1]
        else:
            i1 += 1
            sub = arr[i1:i2 + 1]
        i2 += 1
    if len(sub) > len(r):
        r = sub
    return r


if __name__ == "__main__":
    assert longest_subarray([0, 1, 2, 1, 2, 3]) == [1, 2, 1, 2]
    assert longest_subarray([1, 1, 1, 3, 3, 2, 2]) == [3, 3, 2, 2]
    assert longest_subarray([3, 2, 2, 1]) == [3, 2, 2]
    assert longest_subarray([2, 2, 1]) == [2, 2, 1]
