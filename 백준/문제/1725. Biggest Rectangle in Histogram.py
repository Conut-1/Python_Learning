import sys
input = sys.stdin.readline

n = int(input())
h = [int(input()) for _ in range(n)]

h.append(0)
res = 0
stack = []
for i in range(0, n + 1):
    while stack and h[stack[-1]] > h[i]:
        height = h[stack[-1]]
        stack.pop()
        width = i
        if stack:
            width = i - stack[-1] - 1
        res = max(res, height * width)
    stack.append(i)

print(res)
