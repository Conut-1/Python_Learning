N, B, W = map(int, input().split())
stones = input()

start = 0
stone_count = {"W": 0, "B": 0}
res = 0

for end in range(N):
    stone_count[stones[end]] += 1
    while stone_count["B"] > B and start < end:
        stone_count[stones[start]] -= 1
        start += 1
    if stone_count["W"] >= W and stone_count["B"] <= B:
        res = max(res, end - start + 1)

print(res)
