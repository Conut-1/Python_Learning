n = int(input())
slimes = list(map(int, input().split()))

slimes.sort()

prefix_sum = 0
res = 0
for i in range(n - 1):
    prefix_sum += slimes[i]
    res += prefix_sum * slimes[i + 1]

print(res)
