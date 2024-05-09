from itertools import combinations

n, l, r, x = map(int, input().split())
difficulties = list(map(int, input().split()))

count = 0
for i in range(1, n + 1):
    for c in combinations(difficulties, i):
        diff_list = sorted(list(c))
        if diff_list[-1] - diff_list[0] >= x and l <= sum(diff_list) <= r:
            count += 1

print(count)
