import string


def alphabet_ragnoli(number):
    r = string.ascii_lowercase[0:number]
    l = string.ascii_lowercase[number - 1:0:-1]
    c = "-".join(l + r)
    t = len(c)
    for i in range(1, number)[::-1]:
        r = string.ascii_lowercase[i:number]
        l = string.ascii_lowercase[number - 1:i:-1]
        center = "-".join(l + r)
        print(center.center(t, '-'))

    print(c.center(t, '-'))

    for i in range(1, number):
        r = string.ascii_lowercase[i:number]
        l = string.ascii_lowercase[number - 1:i:-1]
        center = "-".join(l + r)
        print(center.center(t, '-'))


if __name__ == '__main__':
    alphabet_ragnoli(5)
