n = int(input())
met = set()

for _ in range(n):
    a, b = input().split()
    if a == "ChongChong" or b == "ChongChong" or a in met or b in met:
        met.add(a)
        met.add(b)

print(len(met))
