import sys
input = sys.stdin.readline

N = int(input())
pos = []
for _ in range(N):
    pos.append(list(map(float, input().split())))
pos.append(pos[0])

a = 0
b = 0
for i in range(N):
    a += pos[i][0] * pos[i + 1][1]
    b += pos[i][1] * pos[i + 1][0]

print(f'{abs((b - a) / 2):.1f}')
