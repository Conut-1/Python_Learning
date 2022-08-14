def parametric_search():
    high = n * n
    low = 1
    while low <= high:
        mid = (high + low) // 2
        count = 0
        for i in range(1, n + 1):
            count += min(mid // i, n)
        if count < k:
            low = mid + 1
        else:
            high = mid - 1
    return low


n = int(input())
k = int(input())

res = parametric_search()

print(res)
