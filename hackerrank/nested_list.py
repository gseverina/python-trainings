if __name__ == '__main__':
    s = [[5.0, 'Harry'],[5.0, 'Haaa'], [37.21, 'Berry'], [37.21, 'Tina'], [41.0, 'Aaa'], [39, 'Bbb']]
    s.sort()
    print(s)
    t = sorted(set([x[0] for x in s]))
    print(t)
    v = t[1]
    for x in s:
        if x[0] == v:
            print(x[1])
