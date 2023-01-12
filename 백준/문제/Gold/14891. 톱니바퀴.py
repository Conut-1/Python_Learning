import sys
input = sys.stdin.readline


def rotate(gear, direction):
    if direction == 1:
        return gear[-1] + gear[:-1]
    if direction == -1:
        return gear[1:] + gear[0]

def solve(gear_idx, direction):
    rotated[gear_idx] = 1
    if gear_idx < 3 and not rotated[gear_idx + 1] and gears[gear_idx][2] != gears[gear_idx + 1][6]:
        solve(gear_idx + 1, direction * (-1))
    if gear_idx > 0 and not rotated[gear_idx - 1] and gears[gear_idx][6] != gears[gear_idx - 1][2]:
        solve(gear_idx - 1, direction * (-1))
    gears[gear_idx] = rotate(gears[gear_idx], direction)
    rotated[gear_idx] = 0


gears = [input().rstrip() for _ in range(4)]
K = int(input())

rotated = [0] * 4
for _ in range(K):
    gear_idx, direction = map(int, input().split())
    solve(gear_idx - 1, direction)

print(int(gears[0][0]) + int(gears[1][0]) * 2 + int(gears[2][0]) * 4 + int(gears[3][0]) * 8)
