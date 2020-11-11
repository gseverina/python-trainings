from itertools import groupby
n = 13
b = bin(n)[2:]
print(b)
count_dups = [sum(1 for _ in group if _ == '1') for _, group in groupby(b)]
print(count_dups)
print(max(count_dups))

