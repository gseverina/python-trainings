from itertools import product


def cartesian_product(a, b):
    l = []
    for x in product(a, b):
        l.append(x)
    print(' '.join(map(str, l)))

if __name__ == '__main__':
    A = [1, 2] #list(map(int, input().split()))
    B = [3, 4] #list(map(int, input().split()))
    cartesian_product(A, B)

