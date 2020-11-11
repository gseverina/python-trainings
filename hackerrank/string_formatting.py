def print_formatted(number):
    l = len(f'{number:b}') + 1
    for i in range(1, number+1):
        s = f'{i}'.rjust(l) + f' {i:o}'.rjust(l) + f' {i:X}'.rjust(l) + f' {i:b}'.rjust(l)
        print(s)


if __name__ == '__main__':
    print_formatted(16)
