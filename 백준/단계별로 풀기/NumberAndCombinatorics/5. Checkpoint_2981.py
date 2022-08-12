def gcf(x, y):
    if x % y == 0:
        return y
    else:
        return gcf(y, x % y)
    
import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [int(input().strip()) for _ in range(n)]

arr.sort()
x = arr[1] - arr[0]
for i in range(2, n):
    y = arr[i] - arr[0]
    if x == 0 or y == 0:
        x = max(x, y)
    else:
        x = gcf(x, y)
result = set()
for j in range(2, int(x ** 0.5) + 1):
    if (x % j == 0):
        result.add(j)
        result.add(x // j)
result.add(x)
result = sorted(list(result))

print(" ".join(map(str, result)))

# import sys
# input = sys.stdin.readline

# n = int(input().strip())
# arr = [int(input().strip()) for _ in range(n)]

# arr.sort()
# result = []

# flag = 0
# i = arr[1] - arr[0]
# mod = arr[0] % i
# for el in arr:
#     if el % i != mod:
#         mod = -1
#         break
# if mod > -1:
#     flag = 1
# if (flag == 0):
#     i = (arr[1] - arr[0]) // 2
#     while i > 1:
#         mod = arr[0] % i
#         for el in arr:
#             if el % i != mod:
#                 mod = -1
#                 break
#         if mod > -1:
#             break
#         i -= 1

# for j in range(2, round(i ** 0.5) + 1):
#     if i % j  == 0:
#         result.append(j)
#         if j != i // j:
#             result.append(i // j)
# result.append(i)
# result.sort()

# print(" ".join(map(str, result)))
