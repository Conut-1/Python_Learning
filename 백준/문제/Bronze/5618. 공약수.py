from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

common_factor = []
for a, b in combinations(arr, 2):
    while True:
        if a < b:
            a, b = b, a
        a %= b
        if a == 0:
            common_factor.append(b)
            break

mcf = min(common_factor)
res = []
for i in range(1, int(mcf ** 0.5) + 1):
    if mcf % i == 0:
        res.append(i)

res_2 = []
for i in res:
    if mcf // i != i:
        res_2.append(mcf // i)
res_2.reverse()

res = res + res_2

for num in res:
    print(num)
