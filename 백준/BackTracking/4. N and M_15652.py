def dfs(arr, n, m, i):
    if i == m:
        print(" ".join(map(str, arr)))
    else:
        for j in range(1, n + 1):
            if i == 0:
                arr.append(j)
                dfs(arr, n, m, i + 1)
                arr.pop()
            elif arr[i - 1] <= j:
                arr.append(j)
                dfs(arr, n, m, i + 1)
                arr.pop()

n, m = map(int, input().split())

arr = []
dfs(arr, n, m, 0)
