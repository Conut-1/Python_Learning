from itertools import combinations

V, P, L = map(int, input().split())
villages = list(map(int, input().split()))

min_sum = float("inf")
target_villages = []
for posts in combinations(villages, P):
    cur_sum = 0
    for village in villages:
        min_dist = float("inf")
        for post in posts:
            cur_dist = min(abs(village - post), L - abs(village - post))
            min_dist = min(min_dist, cur_dist)
        cur_sum += min_dist
    if min_sum > cur_sum:
        min_sum = cur_sum
        target_villages = list(posts)

print(min_sum)
print(*target_villages)
