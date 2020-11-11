import math


def meal_cost(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    print(f'tip: {tip}')
    tax = meal_cost * (tax_percent / 100)
    print(f'tax: {tax}')
    total = meal_cost + tip + tax
    print(f'total: {total}')
    total_dec, total = math.modf(total)
    print(f'result: {int(total)}')

    return total


if __name__ == "__main__":
    assert meal_cost(0.1, 20, 11) == 15
