def diagonal_difference(arr):
    i = j = 0
    s1 = 0
    while i < len(arr[0]):
        s1 += arr[i][j]
        i += 1
        j += 1

    j = len(arr[0]) - 1
    i = 0
    s2 = 0
    while i < len(arr[0]):
        s2 += arr[i][j]
        i += 1
        j -= 1

    return abs(s1 - s2)


if __name__ == '__main__':
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]
    ]
    assert diagonal_difference(arr) == 2

    arr = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]
    assert diagonal_difference(arr) == 15
