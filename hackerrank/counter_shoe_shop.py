from collections import Counter


if __name__ == '__main__':
    n = int(input())
    l = [int(x) for x in input().split()]
    stock = Counter(l)
    c = int(input())
    s = 0
    for _ in range(c):
        t = [int(x) for x in input().split()]
        ss = t[0]
        if ss in stock.keys():
            if stock[ss] > 0:
                s += t[1]
                stock[ss] -= 1
    print(s)

