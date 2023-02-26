N = int(input())
participants = [tuple(map(int, input().split())) for _ in range(N)]

participants.sort(key=lambda x: x[2], reverse=True)

awarded_nation = []
count = 0
for p in participants:
    if awarded_nation.count(p[0]) == 2:
        continue
    print(p[0], p[1])
    awarded_nation.append(p[0])
    count += 1
    if count == 3:
        break
