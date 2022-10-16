from itertools import permutations
import math

stats = list(map(int, input().split()))

count = 0
for a in permutations(stats, 8):
    check = True
    for i in range(8):
        ccw = a[i % 8] * a[(i + 1) % 8] * math.cos(math.pi / 4) + a[(i + 1) % 8] * a[(i + 2) % 8] * math.sin(math.pi / 4) - a[i % 8] * a[(i + 2) % 8]
        if ccw < 0:
            check = False
    if check == True:
        count += 1

print(count)
