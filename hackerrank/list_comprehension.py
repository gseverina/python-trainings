def print_list(x, y, z, n):
    print([[xi, yi, zi] for xi in range(x+1) for yi in range(y+1) for zi in range(z+1) if (xi+yi+zi) != 3])


if __name__ == "__main__":
    print_list(1, 1, 2, 3)
