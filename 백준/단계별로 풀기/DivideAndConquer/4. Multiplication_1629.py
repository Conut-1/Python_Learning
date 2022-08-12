def square(a, b, c):
    if c == 1:
        return 0
    if b == 0:
        return 1
    if b % 2 == 0:
        return square(a * a % c, b // 2, c) % c
    else:
        return square(a * a % c, b // 2, c) * a % c


a, b, c = map(int, input().split())
print(square(a, b, c))
