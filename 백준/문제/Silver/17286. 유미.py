from itertools import permutations

start = list(map(int, input().split()))
pos = [list(map(int, input().split())) for _ in range(3)]

res = float("inf")
for seq in permutations(pos, 3):
    cur_x, cur_y = start
    dist = 0
    for next_x, next_y in seq:
        dist += ((next_x - cur_x) ** 2 + (next_y - cur_y) ** 2) ** 0.5
        cur_x, cur_y = next_x, next_y
    res = min(res, dist)

print(int(res))
