import math


n = int(input())
numbers = map(int, input().split())
cnt = 0
for num in numbers:
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
            cnt += 1
print(cnt)