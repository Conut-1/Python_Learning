n = int(input())
arr = list(map(int, input().split()))

res = arr[0]
sum = -1001
for num in arr:
    if sum == -1001:
        sum = arr[0]
    elif sum < 0:
        if num > res:
            res = num
        sum = num
    elif num >= 0:
        sum += num
    else:
        if res < sum:
            res = sum
        if sum + num >= 0:
            sum += num
        else:
            sum = num
if sum > res:
    res = sum

print(res)

# 다른 사람 풀이
# n = int(input())
# input_array = list(map(int,input().split()))

# mem = list()
# now = 0
# if max(input_array) <= 0:
#     print(max(input_array))
# else:
#     for num in input_array:
#         if now + num <= 0:
#             now = 0
#             continue
#         now += num
#         mem.append(now)
#     print(max(mem))

# 다른 사람 풀이 2
# n = int(input())
# nums = list(map(int, input().split(' ')))

# d = [0] *(n)
# d[0] = nums[0]

# for i in range(1,n):
#     d[i] = max(nums[i], d[i-1] + nums[i])


# print(max(d))
