import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a_arr = [int(input()) for _ in range(n)]

a_arr.sort()
diff = [a_arr[i + 1] - a_arr[i] for i in range(n - 1)]
start = 0
res = 2_000_000_001
cur = 0
for end in range(n - 1):
    cur += diff[end]
    if cur >= m and cur < res:
        res = cur
    while cur > m and start <= end:
        cur -= diff[start]
        start += 1
        if cur >= m and cur < res:
            res = cur
    if res == m:
        break

print(res)
