import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
height = [0] * 257
highest = 0
for _ in range(N):
    for h in map(int, input().split()):
        height[h] += 1
        highest = max(highest, h)

res_time = float("inf")
res_height = highest
for target_h in range(highest, -1, -1):
    dig_count = 0
    stack_count = 0
    for cur_h in range(257):
        if height[cur_h] and cur_h < target_h:
            stack_count += (target_h - cur_h) * height[cur_h]
        elif height[cur_h] and cur_h > target_h:
            dig_count += (cur_h - target_h) * height[cur_h]

    if dig_count + B < stack_count:
        continue

    if res_time > dig_count * 2 + stack_count:
        res_time = dig_count * 2 + stack_count
        res_height = target_h

print(res_time, res_height)
