def oddNumbers(l, r):
    ret = []
    while l <= r:
        if l % 2 == 0:
            l += 1
        else:
            ret.append(l)
            l += 2
        return ret


if __name__ == "__main__":
    assert(2, 5) == [3, 5]
    assert(3, 9) == [3, 5, 7, 9]
