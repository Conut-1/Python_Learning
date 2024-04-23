def calculate(n, x):
    if x == 0:
        return 0
    if x >= 2 ** (n + 2) - 3:
        return 2 ** (n + 1) - 1
    sum = calculate(n - 1, x - 1)
    if x > 2 ** (n + 1) - 2:
        sum += 1
    if x > 2 ** (n + 1) - 1:
        sum += calculate(n - 1, x - 2 ** (n + 1) + 1)
    return sum


n, x = map(int, input().split())

print(calculate(n, x))
