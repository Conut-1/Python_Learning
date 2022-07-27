import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

sum = sum(arr)
arr = sorted(arr)
min = arr[0]
max = arr[n - 1]
mid = arr[n // 2]
average = round(sum / n)
range = max - min

count = {}
count_max = 0
mode_1 = -4001
mode_2 = -4001
for num in arr:
    if num in count:
        count[num] = count[num] + 1
    else:
        count[num] = 1
for k in count.keys():
    if count[k] > count_max:
        count_max = count[k]
        mode_1 = k
    elif count[k] == count_max and mode_1 > mode_2:
        mode_2 = k

print(average)
print(mid)
if mode_1 > mode_2:
    print(mode_1)
else:
    print(mode_2)
print(range)
