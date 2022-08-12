import sys
input = sys.stdin.readline


def parametric_search():
    high = max(cable)
    low = 1
    while low <= high:
        mid = (high + low) // 2
        num = 0
        for len in cable:
            num += len // mid
        if num < n:
            high = mid - 1
        else:
            low = mid + 1
    return high


k, n = map(int, input().split())
cable = [int(input()) for _ in range(k)]

res = parametric_search()

print(res)
