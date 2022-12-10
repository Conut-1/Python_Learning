def dfs(index):
    if index == M:
        print(*arr)
    else:
        for num in numbers:
            if num not in arr:
                arr.append(num)
                dfs(index + 1)
                arr.pop()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

arr = []
dfs(0)
