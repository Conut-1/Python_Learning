from itertools import combinations

n = int(input())
res = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        res.append(int("".join(map(str, num))))

res.sort()
print(res[n] if len(res) > n else -1)
