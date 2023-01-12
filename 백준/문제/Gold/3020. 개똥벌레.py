import sys
input = sys.stdin.readline

N, H = map(int, input().split())
top = [0] * (H + 1)
bottom = [0] * (H + 1)

for i in range(N):
    obstacle = int(input())
    if i % 2 == 0:
        bottom[obstacle] += 1
    else:
        top[-obstacle] += 1

for i in range(1, H + 1):
    top[i] += top[i - 1]
    bottom[-1 - i] += bottom[-i]

count = 0
ans = 200_001
for i in range(1, H + 1):
    if top[i] + bottom[i] < ans:
        count = 1
        ans = top[i] + bottom[i]
    elif top[i] + bottom[i] == ans:
        count += 1

print(ans, count)
