import sys

input = sys.stdin.readline

m, n = map(int, input().split())

universes = dict()
for _ in range(m):
    universe = list(map(int, input().split()))
    compression = sorted(set(universe))
    comp_dict = {c: i for i, c in enumerate(compression)}
    universe = tuple(map(lambda x: comp_dict[x], universe))
    if universe not in universes:
        universes[universe] = 0
    universes[universe] += 1

count = 0
for i in universes.values():
    count += (i * (i - 1)) // 2

print(count)
