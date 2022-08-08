n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr2 = [0] * m
arr2[0] = 1
sum = 0
for num in arr:
    sum += num
    arr2[sum % m] += 1

count = 0
for el in arr2:
    count += el * (el - 1) // 2

print(count)
