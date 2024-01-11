n = int(input())
arr = list(map(int, input().split()))

max_length = 1
up_count = 1
down_count = 1

for i in range(1, len(arr)):
    if arr[i - 1] > arr[i]:
        up_count = 1
        down_count += 1
    elif arr[i - 1] == arr[i]:
        up_count += 1
        down_count += 1
    else:
        up_count += 1
        down_count = 1
    max_length = max(max_length, up_count, down_count)

print(max_length)
