import sys
input = sys.stdin.readline

N = int(input())
players = [list(map(int, input().split())) for _ in range(N)]

for i in range(3):
    for j in range(N):
        tmp = players[j][i]
        for k in range(j + 1, N):
            if tmp == players[k][i]:
                players[j][i] = 0
                players[k][i] = 0
            
for cards in players:
    print(sum(cards))
