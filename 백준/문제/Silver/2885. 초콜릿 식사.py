K = int(input())

chocolate = 0
for i in range(20 + 1):
    if 2 ** i >= K:
        chocolate = 2 ** i
        break

split = 0
cur = chocolate
has = 0
while has < K:
    if cur > K - has:
        cur //= 2
        split += 1
    else:
        has += cur

print(chocolate, split)
