from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

result = 0
for i in combinations(card, 3):
    if result < sum(i) and sum(i) <= m:
        result = sum(i)
print(result)

# n, m = map(int, input().split())
# card = list(map(int, input().split()))

# result = 0
# for i in range(n - 2):
#     for j in range(i + 1, n - 1):
#         for k in range(j + 1, n):
#             sum = card[i] + card[j] + card[k]
#             if (m >= sum and sum > result):
#                 result = sum
# print(result)