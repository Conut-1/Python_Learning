from collections import deque


n, k = map(int, input().split())

queue = deque([n])
time = [-1] * 100001
time[n] = 0
res = 0
while queue:
    r = queue.popleft()
    if r == k:
       res = time[r]
       break
    if 0 <= 2 * r < 100001 and time[2 * r] == -1:
        time[2 * r] = time[r]
        queue.appendleft(2 * r)
    for next in (r - 1, r + 1):
        if 0 <= next < 100001 and time[next] == -1:
            time[next] = time[r] + 1
            queue.append(next)

print(res)
