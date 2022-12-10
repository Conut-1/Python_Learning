def dfs(index):
    if index == M:
        print(*arr)
    else:
        for num in numbers:
            if index == 0:
                arr.append(num)
                dfs(index + 1)
                arr.pop()
            elif arr[index - 1] <= num:
                arr.append(num)
                dfs(index + 1)
                arr.pop()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

arr = []
dfs(0)
