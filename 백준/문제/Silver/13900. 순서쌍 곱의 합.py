N = int(input())
num = list(map(int, input().split()))

sum = sum(num)
res = 0
for n in num:
    res += n * (sum - n)
res //= 2

print(res)
