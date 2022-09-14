N = int(input())
arr = list(map(int, input().split()))

memoization = [-1000000001]
idx = [0] * N
for i in range(N):
    if memoization[-1] < arr[i]:
        memoization.append(arr[i])
        idx[i] = len(memoization) - 1
    else:
        left = 0
        right = len(memoization)
        while left < right:
            mid = (left + right) // 2
            if memoization[mid] < arr[i]:
                left = mid + 1
            else:
                right = mid
        memoization[right] = arr[i]
        idx[i] = right

res_len = len(memoization) - 1
print(res_len)
res = []
for i in range(N - 1, -1, -1):
    if res_len == idx[i]:
        res.append(arr[i])
        res_len -= 1
res.reverse()
print(*res)
