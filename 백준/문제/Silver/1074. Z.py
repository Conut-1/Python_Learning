import sys
sys.setrecursionlimit(10 ** 6)

def divide(x, y, n):
    global count

    if x == r and y == c:
        print(count)
        exit(0)
    if not (x <= r < x + 2 ** n and y <= c < y + 2 ** n):
        count += (2 ** n) ** 2
        return
    divide(x, y, n - 1)
    divide(x, y + 2 ** (n - 1), n - 1)
    divide(x + 2 ** (n - 1), y, n - 1)
    divide(x + 2 ** (n - 1), y + 2 ** (n - 1), n - 1)

N, r, c = map(int, input().split())

count = 0
divide(0, 0, N)
