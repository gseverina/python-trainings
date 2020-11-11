# GCD: Greatest Common Denominator
def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b

    return b


if __name__ == "__main__":
    assert gcd(60, 96) == 12
    assert gcd(20, 8) == 4
