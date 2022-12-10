N = int(input())
M = int(input())
if M:
    broken = set(input().split())
else:
    broken = set()

min_cnt = abs(100 - N)

for k in range(1000000):
    num = str(k)
    for n in num:
        if n in broken:
            break
    else:
        min_cnt = min(min_cnt, abs(N - k) + len(num))

print(min_cnt)
