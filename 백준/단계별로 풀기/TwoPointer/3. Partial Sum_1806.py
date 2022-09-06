n, s = map(int, input().split())
arr = list(map(int, input().split()))

j = 0
sum = 0
res = n + 1
for i in range(n):
    while sum < s and j < n:
        sum += arr[j]
        j += 1
    if sum >= s:
        res = min(res, j - i)
    sum -= arr[i]

print(0 if res == n + 1 else res)
