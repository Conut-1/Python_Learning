from collections import deque


n, k = map(int, input().split())

queue = deque([n])
time = [0] * 100001
time[n] = 0
res = 0
while queue:
    r = queue.popleft()
    if r == k:
       res = time[r]
       break
    for next in (r - 1, r + 1, 2 * r):
        if 0 <= next < 100001 and not time[next]:
            time[next] = time[r] + 1
            queue.append(next)

print(res)


# from collections import deque


# n, k = map(int, input().split())

# queue = deque()
# time = {}
# time[n] = 0
# queue.append(n)
# res = 0
# while queue:
#     r = queue.popleft()
#     if r == k:
#        res = time[r]
#        break 
#     if not r + 1 in time:
#         time[r + 1] = time[r] + 1
#         queue.append(r + 1)
#     if r >= 0 and not r - 1 in time:
#         time[r - 1] = time[r] + 1
#         queue.append(r - 1)
#     if r < k + 1 and not 2 * r in time:
#         time[2 * r] = time[r] + 1
#         queue.append(2 * r)

# print(res)
