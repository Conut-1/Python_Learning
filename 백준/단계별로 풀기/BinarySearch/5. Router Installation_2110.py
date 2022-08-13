import sys
input = sys.stdin.readline


def parametric_search():
    high = pos[-1] - pos[0]
    low = 1
    while low <= high:
        mid = (high + low) // 2
        count = 1
        cur = pos[0]
        for x in pos:
            if x - cur >= mid:
                count += 1
                cur = x
        if count >= c:
            low = mid + 1
        else:
            high = mid - 1
    return high


n, c = map(int, input().split())
pos = [int(input()) for _ in range(n)]

pos.sort()
res = parametric_search()

print(res)
