def dfs(arr, n, m, i):
    if i == m:
        print(" ".join(map(str, arr)))
    else:
        for j in range(1, n + 1):
            if not j in arr[0:i]:
                arr[i] = j
                dfs(arr, n, m, i + 1)

n, m = map(int, input().split())

arr = [0] * m
dfs(arr, n, m, 0)
