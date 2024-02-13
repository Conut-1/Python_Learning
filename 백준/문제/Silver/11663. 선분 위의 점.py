import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

for _ in range(m):
    a, b = map(int, input().split())

    if b < arr[0] or a > arr[-1]:
        print(0)
        continue

    left = 0
    right = len(arr) - 1

    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == a:
            end = mid
            break
        elif arr[mid] > a:
            end = mid
        else:
            start = mid + 1
    left = end

    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == b:
            end = mid
            break
        elif arr[mid] > b:
            end = mid - 1
        else:
            start = mid + 1
    right = end

    print(right - left + 1 if right >= left else 0)
