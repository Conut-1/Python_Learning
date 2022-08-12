def matrix_mul(a, b):
    res = [[0] * n for _ in range(n)]
    for i in range(n * n):
        sum = 0
        for j in range(n):
            sum += a[i // n][j] * b[j][i % n]
        res[i // n][i % n] = sum % 1000
    return res


def square(matrix, b):
    if b == 1:
        return matrix
    if b % 2 == 0:
        return square(matrix_mul(matrix, matrix), b // 2)
    else:
        return matrix_mul(square(matrix_mul(matrix, matrix), b // 2), matrix)


n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

res = square(matrix, b)
for i in range(n * n):
    res[i // n][i % n] %= 1000

for line in res:
    print(*line)
