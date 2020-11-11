def bouncing_ball(h, bounce, window):
    if h < 0:
        return -1

    if bounce <= 0 or bounce >= 1:
        return -1

    if window >= h:
        return -1

    i = 1
    while True:
        r = h * bounce
        if r <= window:
            return i
        i += 2
        h = r


if __name__ == "__main__":
    assert bouncing_ball(3, 1, 1.5) == -1
    assert bouncing_ball(2, 0.5, 1) == 1
    assert bouncing_ball(3, 0.66, 1.5) == 3
    assert bouncing_ball(30, 0.66, 1.5) == 15
    assert bouncing_ball(30, 0.75, 1.5) == 21