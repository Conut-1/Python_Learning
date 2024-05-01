n, k = map(int, input().split())
heights = list(map(int, input().split()))

diff = [heights[i + 1] - heights[i] for i in range(n - 1)]
diff.sort()

print(sum(diff[: n - k]))
