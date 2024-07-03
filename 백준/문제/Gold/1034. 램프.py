N, M = map(int, input().split())
lamps = [input() for _ in range(N)]
K = int(input())

max_count = 0
for i in range(N):
    zero_count = 0
    for lamp in lamps[i]:
        if lamp == "0":
            zero_count += 1

    same_cnt = 0
    if zero_count <= K and zero_count % 2 == K % 2:
        for j in range(N):
            if lamps[i] == lamps[j]:
                same_cnt += 1

    max_count = max(max_count, same_cnt)

print(max_count)
