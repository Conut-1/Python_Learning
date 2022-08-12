def binary_search(n, num):
    high = n - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        if a[mid] == num:
            return 1
        elif a[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return 0


n = int(input())
a = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

a.sort()
for num in target:
    res = binary_search(n, num)
    print(res)
