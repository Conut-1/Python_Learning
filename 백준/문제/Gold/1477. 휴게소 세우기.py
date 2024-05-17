N, M, L = map(int, input().split())
areas = list(map(int, input().split()))

areas.extend([0, L])
areas.sort()
start = 1
end = L


def check(l):
    count = 0
    for i in range(1, len(areas)):
        step = areas[i] - areas[i - 1]
        count += step // l
        if step % l == 0:
            count -= 1
    return count <= M


while start < end:
    mid = (start + end) // 2
    if check(mid):
        end = mid
    else:
        start = mid + 1

print(end)
