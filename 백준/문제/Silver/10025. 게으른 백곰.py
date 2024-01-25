import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = [0] * 1_000_000
max_x = 0
for _ in range(n):
    g, x = map(int, input().split())
    arr[x - 1] = g
    max_x = max(max_x, x - 1)

window_sum = sum(arr[: 2 * k + 1])
res = []
res.append(window_sum)
for i in range(2 * k + 1, max_x + 1):
    window_sum = window_sum + arr[i] - arr[i - 2 * k - 1]
    res.append(window_sum)

print(max(res))
