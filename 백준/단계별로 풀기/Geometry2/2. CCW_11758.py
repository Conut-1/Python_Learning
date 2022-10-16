pos = []
for _ in range(3):
    pos.append(list(map(int, input().split())))
pos.append(pos[0])

a = 0
b = 0
for i in range(3):
    a += pos[i][0] * pos[i + 1][1]
    b += pos[i][1] * pos[i + 1][0]

ccw = a - b

if ccw == 0:
    print(0)
elif ccw < 0:
    print(-1)
else:
    print(1)
