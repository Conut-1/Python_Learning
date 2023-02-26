N = int(input())
cows = [tuple(map(int, input().split())) for _ in range(N)]

cows.sort()
time = 0
for cow in cows:
    if time < cow[0]:
        time = cow[0]
    time += cow[1]

print(time)
