import sys
input = sys.stdin.readline

R, C = map(int, input().split())
picture = [input().strip() for _ in range(R)]
picture.sort()

prev = -1
rank = 0
res = [0] * 9
for line in picture:
    for i in range(1, C - 1):
        if line[i] != '.':
            remain = C - i - 4
            if prev != remain:
                rank += 1
            res[int(line[i]) - 1] = rank
            prev = remain
            break

for rank in res:
    print(rank)
