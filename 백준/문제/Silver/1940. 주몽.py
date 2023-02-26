N = int(input())
M = int(input())
arr = list(map(int, input().split()))

arr.sort()
i = 0
j = N - 1
count = 0
while i < j:
    if arr[i] + arr[j] == M:
        i += 1
        j -= 1
        count += 1
    elif arr[i] + arr[j] > M:
        j -= 1
    else:
        i += 1

print(count)
