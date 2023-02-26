import sys
input = sys.stdin.readline

def gcf(a, b):
    while b:
        a, b = b, a % b
    return a
    
N = int(input())
colonnades = [int(input()) for _ in range(N)]

dist = colonnades[1] - colonnades[0]
for i in range(1, N - 1):
    new_dist = colonnades[i + 1] - colonnades[i]
    dist = gcf(dist, new_dist)

res = (colonnades[-1] - colonnades[0]) // dist - N + 1

print(res)
