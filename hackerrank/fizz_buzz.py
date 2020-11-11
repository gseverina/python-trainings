def fizz_buzz(n):
    # Write your code here
    p = ""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            p = "FizzBuzz"
        elif i % 3 == 0:
            p = "Fizz"
        elif i % 5 == 0:
            p = "Buzz"
        else:
            p = i
        print(f'{p}.')


if __name__ == "__main__":
    fizz_buzz(15)
