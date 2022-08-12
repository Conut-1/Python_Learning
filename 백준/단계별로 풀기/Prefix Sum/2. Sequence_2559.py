n, k = map(int, input().split())
temperature = list(map(int, input().split()))

temp_sum = [0]
temp = 0
for num in temperature:
    temp += num
    temp_sum.append(temp)

res = temp_sum[k] - temp_sum[0]
for i in range(k + 1, n + 1):
    partial_sum = temp_sum[i] - temp_sum[i - k]
    if res < partial_sum:
        res = partial_sum

print(res)
