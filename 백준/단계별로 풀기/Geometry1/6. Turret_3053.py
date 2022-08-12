from math import dist
import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    distance = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5
    if distance < r_1 or distance < r_2:
        if distance == 0 and r_1 == r_2:
            print(-1)
        elif distance < abs(r_1 - r_2):
            print(0)
        elif distance == abs(r_1 - r_2):
            print(1)
        else:
            print(2)
    else:
        if distance > r_1 + r_2:
            print(0)
        elif distance == r_1 + r_2:
            print(1)
        else:
            print(2)
