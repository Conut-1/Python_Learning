from collections import deque


n, k = map(int, input().split())

queue = deque([n])
time = [0] * 100001
time[n] = 0
res_sec = 0
while queue:
    r = queue.popleft()
    if r == k:
       res_sec = time[r]
       break
    for next in (r - 1, r + 1, 2 * r):
        if 0 <= next < 100001 and not time[next]:
            time[next] = time[r] + 1
            queue.append(next)

print(res_sec)

cur_sec = res_sec
res_pos = []
cur_pos = k
while cur_sec:
    res_pos.append(cur_pos)
    cur_sec -= 1
    if cur_sec == 0:
        continue
    if 0 <= cur_pos - 1 < 100001 and time[cur_pos - 1] == cur_sec:
        cur_pos -= 1
    elif 0 <= cur_pos + 1 < 100001 and time[cur_pos + 1] == cur_sec:
        cur_pos += 1
    elif cur_pos % 2 == 0 and time[cur_pos // 2]:
        cur_pos //= 2
res_pos.append(n)
res_pos.reverse()

print(*res_pos)
