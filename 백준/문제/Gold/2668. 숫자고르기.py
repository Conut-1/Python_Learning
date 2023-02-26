import sys
input = sys.stdin.readline

def dfs(cur, start):
    if visited[cur]:
        if cur == start:
            res.append(start)
    else:
        visited[cur] = 1
        dfs(numbers[cur], start)

N = int(input())
numbers = [0] + [int(input()) for _ in range(N)]
res = []

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    dfs(i, i)

print(len(res))
for num in res:
    print(num)
