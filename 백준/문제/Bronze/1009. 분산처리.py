import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    data = 1
    while b != 0:
        if b % 2 == 1:
            data = data * a % 10
        a = a * a % 10
        b //= 2
    if data == 0:
        data = 10
    print(data)
