import sys
input = sys.stdin.readline


N = int(input())
x, y = map(int, input().split())
x_left = x
x_right = x
y_up = y
y_down = y
for _ in range(N - 1):
    x, y = map(int, input().split())
    if x < x_left:
        x_left = x
    if x > x_right:
        x_right = x
    if y < y_down:
        y_down = y
    if y > y_up:
        y_up = y

print((x_right - x_left) * (y_up - y_down))
