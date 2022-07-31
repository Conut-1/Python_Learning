n = int(input())
minimum = n - len(str(n)) * 9
if minimum < 0:
    minimum = 0
result = 0
for i in range(minimum, n):
    sum = i
    for j in str(i):
        sum += int(j)
    if sum == n:
        result = i
        break
print(result)

# n = int(input())
# result = 0
# for i in range(n):
#     tmp = i
#     sum = i
#     while tmp:
#         sum += tmp % 10
#         tmp //= 10
#     if sum == n:
#         result = i
#         break
# print(result)