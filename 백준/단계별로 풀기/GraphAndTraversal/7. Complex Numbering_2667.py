import sys
sys.setrecursionlimit(100000)


def dfs(r):
    global count

    map[r // n][r % n] = "0"
    count += 1
    if r // n > 0 and map[r // n - 1][r % n] == "1":
        dfs(r - n)
    if r // n < n - 1 and map[r // n + 1][r % n] == "1":
        dfs(r + n)
    if r % n > 0 and map[r // n][r % n - 1] == "1":
        dfs(r - 1)
    if r % n < n - 1 and map[r // n][r % n + 1] == "1":
        dfs(r + 1)


n = int(input())
map = [list(input()) for _ in range(n)]

res = []
for i in range(n * n):
    count = 0
    if map[i // n][i % n] == "1":
        dfs(i)
        res.append(count)
res.sort()

print(len(res))
for size in res:
    print(size)
