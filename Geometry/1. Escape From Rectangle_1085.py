x, y, w, h = map(int, input().split())

len = [x, y, w - x, h - y]
print(min(len))