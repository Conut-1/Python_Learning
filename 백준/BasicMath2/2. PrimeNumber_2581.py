import math

m = int(input())
n = int(input())
arr = []
for num in range(m, n + 1):
    if num == 1:
        continue
    else:
        j = 2
        is_prime = 1
        while j <= math.sqrt(num):
            if num % j == 0:
                is_prime = 0
                break
            j += 1
        if is_prime == 1:
            arr.append(num)
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))