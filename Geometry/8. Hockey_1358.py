import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
count = 0

for _ in range(p):
    p_x, p_y = map(int, input().split())
    if x <= p_x <= x + w and y <= p_y <= y + h:
        count += 1
    elif ((x - p_x) ** 2 + (y + 0.5 * h - p_y) ** 2) ** 0.5 <= 0.5 * h:
        count += 1
    elif ((x + w - p_x) ** 2 + (y + 0.5 * h - p_y) ** 2) ** 0.5 <= 0.5 * h:
        count += 1
print(count)
