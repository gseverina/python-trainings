# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    phone_book = {}
    for _ in range(n):
        name, num = input().split()
        phone_book[name] = num

    try:
        query_name = input()
        while query_name:
            if query_name in phone_book.keys():
                print(f'{query_name}={phone_book[query_name]}')
            else:
                print('Not found')
            query_name = input()
    except EOFError:
        pass
