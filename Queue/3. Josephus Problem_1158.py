from collections import deque
import sys
input = sys.stdin.readline

a = deque([])
b = []
n, k = map(int, input().split())

for i in range(1, n + 1):
    a.append(i)

for i in range(n):
    for j in range(k - 1):
        a.append(a.popleft())
    b.append(str(a.popleft()))

output = ", ".join(b)
print("<{}>".format(output))