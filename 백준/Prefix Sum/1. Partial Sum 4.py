import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum = [0]
temp = 0
for num in arr:
    temp += num
    sum.append(temp)

for i in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i - 1])
