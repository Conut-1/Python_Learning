a, b = map(int, input().split())
l, r = 0, 0
while not (a == 1 and b == 1):
    if a > b:
        a -= b
        l += 1
    else:
        b -= a
        r += 1
print(l, r)
