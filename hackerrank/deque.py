from collections import deque

if __name__ == '__main__':
    n = int(input())
    d = deque()
    for _ in range(n):
        task = input().split()
        op = task[0]
        if op == 'append':
            d.append(task[1])
        elif op == 'appendleft':
            d.appendleft(task[1])
        elif op == 'pop':
            d.pop()
        else:
            d.popleft()
    print(" ".join(d))
