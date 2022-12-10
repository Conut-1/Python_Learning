import sys
input = sys.stdin.readline

N = int(input())
u = [int(input()) for _ in range(N)]
u.sort()

x_y = set()
for i in range(len(u)):
    for j in range(i, len(u)):
        x_y.add(u[i] + u[j])

for i in range(len(u)):
    for j in u:
        if (u[-i - 1] - j) in x_y:
            print(u[-i - 1])
            exit(0)
