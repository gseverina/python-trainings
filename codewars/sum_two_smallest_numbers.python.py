

def sum_two_smallest_numbers(numbers):
    s = sorted(numbers)
    return s[0] + s[1]
    

assert sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13
assert sum_two_smallest_numbers([7, 15, 12, 18, 22]) == 19
assert sum_two_smallest_numbers([25, 42, 12, 18, 22]) == 30