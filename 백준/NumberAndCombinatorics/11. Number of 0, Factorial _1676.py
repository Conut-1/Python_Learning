import math

n = int(input())

fac_str = reversed(str(math.factorial(n)))
cnt = 0
for c in fac_str:
    if c != "0":
        break
    cnt += 1

print(cnt)
