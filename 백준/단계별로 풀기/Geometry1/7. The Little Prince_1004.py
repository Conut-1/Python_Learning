import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    n = int(input().strip())
    count = 0

    for __ in range(n):
        c_x, c_y, r = map(int, input().split())
        if bool(((x_1 - c_x) ** 2 + (y_1 - c_y) ** 2) ** 0.5 < r) ^ bool(((x_2 - c_x) ** 2 + (y_2 - c_y) ** 2) ** 0.5 < r):
            count += 1

    print(count)
