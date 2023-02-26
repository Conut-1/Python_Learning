MAX = 1_000_000_000
X, Y = map(int, input().split())

Z = Y * 100 // X
if Z >= 99:
    print(-1)
    exit(0)

low, high = 1, MAX
result = -1
while low <= high:
    mid = (low + high) // 2
    z = (Y + mid) * 100 // (X + mid)
    if Z >= z:
        low = mid + 1
    else:
        high = mid - 1

print(low)
