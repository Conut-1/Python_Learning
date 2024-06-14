import sys

input = sys.stdin.readline

n, m = map(int, input().split())
bosses = [0] + list(map(int, input().split()))
employee = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    if bosses[i] == -1:
        continue
    employee[bosses[i]].append(i)

compliments = [0] * (n + 1)
for _ in range(m):
    i, w = map(int, input().split())
    compliments[i] += w

res = [0] * (n + 1)
stack = [(1, 0)]
while stack:
    cur, compliment = stack.pop()
    compliment += compliments[cur]
    res[cur] = compliment
    for next in employee[cur]:
        stack.append((next, compliment))

print(*(res[1:]))
