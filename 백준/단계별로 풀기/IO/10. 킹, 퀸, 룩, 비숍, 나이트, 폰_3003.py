CORRECT_PIECE = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))

res = []
for i, j in zip(CORRECT_PIECE, arr):
    res.append(i - j)

print(*res)
