n, m = map(int, input().split())
castle = [input() for _ in range(n)]

row = [0] * n
col = [0] * m

for i in range(n):
    for j in range(m):
        if castle[i][j] == 'X':
            row[i] = 1
            col[j] = 1

row_count = row.count(0)
col_count = col.count(0)

print(max(row_count, col_count))
