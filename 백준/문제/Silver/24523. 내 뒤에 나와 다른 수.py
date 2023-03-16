N = int(input())
a = list(map(int, input().split()))

stack = []
res = [-1] * N
for i in range(N):
    while stack and a[stack[-1]] != a[i]:
        res[stack.pop()] = i + 1
    stack.append(i)

print(*res)
