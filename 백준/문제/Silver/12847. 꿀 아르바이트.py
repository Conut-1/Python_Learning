n, m = map(int, input().split())
arr = list(map(int, input().split()))

res = []
window_sum = sum(arr[:m])
res.append(window_sum)

for i in range(m, n):
    window_sum = window_sum - arr[i - m] + arr[i]
    res.append(window_sum)

print(max(res))
