import sys
input = sys.stdin.readline

arr = [True] * (10_000 + 1)
arr[0] = False
arr[1] = False

prime = []
for i in range(2, 10_000 + 1):
    if arr[i] == True:
        prime.append(i)
        for j in range(2, 10_000 // i + 1):
            arr[i * j] = False

T = int(input())
for _ in range(T):
    n = int(input())
    res = [0, 0]
    for num in prime:
        if num > n // 2:
            break

        if arr[n - num] == True:
            res = [num, n - num]

    print(*res)
