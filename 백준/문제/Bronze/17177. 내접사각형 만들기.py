def solve(a, b, c):
    for i in range(1, 100 + 1):
        if 2 * a * b * c * i == (a ** 2) * (a ** 2 - b ** 2 - c ** 2 - i ** 2):
            return i
    return -1


a, b, c = map(int, input().split())
print(solve(a, b, c))
