def dfs(index):
    if index == M:
        print(*arr)
    else:
        for num in numbers:
            if index == 0:
                arr.append(num)
                dict[num] -= 1
                dfs(index + 1)
                dict[arr.pop()] += 1
            elif dict[num]:
                arr.append(num)
                dict[num] -= 1
                dfs(index + 1)
                dict[arr.pop()] += 1

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
dict = {}
for num in numbers:
    if num not in dict:
        dict[num] = 0
    dict[num] += 1
numbers = list(set(numbers))
numbers.sort()

arr = []
dfs(0)
