def parametric_search():
    high = max(tree)
    low = 0
    while low <= high:
        mid = (high + low) // 2
        sum = 0
        for len in tree:
            if len > mid:
                sum += len - mid
        if sum == m:
            return mid
        if sum > m:
            low = mid + 1
        else:
            high = mid - 1
    return high


n, m = map(int, input().split())
tree = list(map(int, input().split()))

res = parametric_search()

print(res)
