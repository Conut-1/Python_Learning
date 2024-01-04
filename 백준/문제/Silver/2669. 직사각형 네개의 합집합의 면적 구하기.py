plane = [[0] * 100 for _ in range(100)]

for _ in range(4):
    rectangle = list(map(int, input().split()))
    for i in range(rectangle[0], rectangle[2]):
        for j in range(rectangle[1], rectangle[3]):
            plane[i][j] = 1

res = 0
for i in range(100):
    res += plane[i].count(1)
print(res)
