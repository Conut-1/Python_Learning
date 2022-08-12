def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res = i * res % p
    return res


def square(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return square(a * a % p, b // 2) % p
    else:
        return square(a * a % p, b // 2) * a % p


n, k = map(int, input().split())
p = 1000000007

dict = {0: 1, 1: 1}
numerator = factorial(n)
denominator = factorial(k) * factorial(n - k) % p
result = numerator * square(denominator, p - 2) % p
print(result)
