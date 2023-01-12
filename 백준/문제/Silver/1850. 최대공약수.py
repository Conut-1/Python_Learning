a, b = map(int, input().split())

if b > a:
    a, b = b, a

while b:
    a %= b
    a, b = b, a

print('1' * a)
