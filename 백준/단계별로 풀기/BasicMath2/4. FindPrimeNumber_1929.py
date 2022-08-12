m, n = map(int, input().split())
arr = [True] * (n + 1)
arr[0] = False
arr[1] = False

for i in range(2, n + 1):
    if arr[i] == True:
        if m <= i <= n:
            print(i)
        for j in range(2, n // i + 1):
            arr[i * j] = False