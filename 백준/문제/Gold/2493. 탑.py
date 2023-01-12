N = int(input())
towers = list(map(int, input().split()))

stack = []
res = [0] * N
for i in range(N):
    while stack and towers[stack[-1] - 1] < towers[i]:
        stack.pop()
    if stack:
        res[i] = stack[-1]
    else:
        res[i] = 0
    stack.append(i + 1)

print(*res)
