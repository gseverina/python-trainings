def max_hour_glass(lst):
    mhg = None
    for i in range(len(lst[0]) - 2):
        for j in range(len(lst) - 2):
            s = sum(lst[j][i:i + 3]) + lst[j + 1][i + 1] + sum(lst[j + 2][i:i + 3])
            if not mhg or s > mhg:
                mhg = s
    return mhg


if __name__ == '__main__':
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    assert max_hour_glass(arr) == 19

    arr = [
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5]
    ]
    assert abs(max_hour_glass(arr)) == abs(-6)

    arr = [
        [0, -4, -6, 0, -7, -6],
        [-1, -2, -6, -8, -3, -1],
        [-8, -4, -2, -8, -8, -6],
        [-3, -1, -2, -5, -7, -4],
        [-3, -5, -3, -6, -6, -6],
        [-3, -6, 0, -8, -6, -7]
    ]
    assert abs(max_hour_glass(arr)) == abs(-19)
