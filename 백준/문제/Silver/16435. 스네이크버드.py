N, L = map(int, input().split())
hs = list(map(int, input().split()))

l = L
hs.sort()

for h in hs:
    if l >= h:
        l += 1

print(l)
