n, x = map(int, input().split())
sequence = list(map(int, input().split()))
under = []
for i in range(n):
    if sequence[i] < x:
        under.append(str(sequence[i]))
print(" ".join(under))