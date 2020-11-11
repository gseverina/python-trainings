def very_big_sum(ar):
    return sum(ar)


if __name__ == '__main__':
    assert very_big_sum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 5000000015

