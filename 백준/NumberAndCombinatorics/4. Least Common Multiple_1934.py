def gcf(a, b):
    if a % b == 0:
        return b
    else:
        return gcf(b, a % b)

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(a * b // gcf(a, b))

# t = int(input())

# for _ in range(t):
#     gcf = 0
#     a, b = map(int, input().split())
#     n_1 = a
#     n_2 = b
#     while gcf == 0:
#         if n_1 > n_2:
#             tmp = n_1
#             n_1 = n_2
#             n_2 = tmp
#         if n_2 % n_1 == 0:
#             gcf = n_1
#         else:
#             n_2 %= n_1
#     print(a * b // gcf)
