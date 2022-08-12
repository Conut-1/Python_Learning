def matrix_mul(a, b):
    res = [[0] * 2 for _ in range(2)]
    for i in range(2 * 2):
        sum = 0
        for j in range(2):
            sum += a[i // 2][j] * b[j][i % 2]
        res[i // 2][i % 2] = sum % m
    return res


def square(matrix, b):
    if b == 1:
        return matrix
    if b % 2 == 0:
        return square(matrix_mul(matrix, matrix), b // 2)
    else:
        return matrix_mul(square(matrix_mul(matrix, matrix), b // 2), matrix)


n = int(input())
m = 1000000007

if n == 1:
    print(1)
else:
    matrix = [[1, 1], [1, 0]]
    res = square(matrix, n - 1)

    print(res[0][0])
