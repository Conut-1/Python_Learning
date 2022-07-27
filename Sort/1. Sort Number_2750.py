arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
for i in range(1, n):
    for j in range(0, i):
        if arr[i - j] < arr[i - j - 1]:
            tmp = arr[i - j]
            arr[i - j] = arr[i - j - 1]
            arr[i - j - 1] = tmp
        else:
            break
for i in arr:
    print(i)
