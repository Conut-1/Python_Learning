n = int(input())

prime = []
arr = [True] * (n + 1)
arr[0] = False
arr[1] = False

for i in range(2, n + 1):
    if arr[i] == True:
        prime.append(i)
        for j in range(2, n // i + 1):
            arr[i * j] = False

j = 0
sum = 0
count = 0
for i in range(len(prime)):
    while sum < n and j < len(prime):
        sum += prime[j]
        j += 1
    if sum == n:
        count += 1
    sum -= prime[i]

print(count)
