def sock_merchant(n, ar):
    ar.sort()
    pairs = 0
    while len(ar) > 1:
        c = ar.count(ar[0])
        if c > 1:
            pairs += int(c / 2)
            ar = ar[c:]
        else:
            ar = ar[1:]
    return pairs


if __name__ == "__main__":
    assert sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3
