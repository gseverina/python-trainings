def sequence(num):
    if num == 1:
        return 1
    else:
        return sequence(num - 1) + 2 * (num - 1)


def row_sum_odd_numbers(row):
    start = sequence(row)
    stop = sequence(row+1)
    r = 0
    for i in range(start, stop, 2):
        r += i
    return r


if __name__ == "__main__":
    assert row_sum_odd_numbers(1) == 1
    assert row_sum_odd_numbers(2) == 8
    assert row_sum_odd_numbers(13) == 2197
    assert row_sum_odd_numbers(19) == 6859
    assert row_sum_odd_numbers(41) == 68921
