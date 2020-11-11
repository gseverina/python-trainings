if __name__ == '__main__':
    l = [int(x) for x in input().split()]
    #l = [9, 27]
    n = l[0]
    m = l[1]
    center = "WELCOME".center(m, "-")
    odds = [x for x in range(1, n) if (x % 2) != 0]
    for i in odds:
        s = ".|." * i
        print(s.center(m, "-"))
    print(center)
    for i in odds[::-1]:
        s = ".|." * i
        print(s.center(m, "-"))
