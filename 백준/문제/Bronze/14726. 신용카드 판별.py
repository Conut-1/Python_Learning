import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    card = list(map(int, input().strip()))
    for i in range(0, 16, 2):
        tmp = card[i] * 2
        if tmp >= 10:
            tmp = tmp // 10 + tmp % 10
        card[i] = tmp
    if sum(card) % 10:
        print("F")
    else:
        print("T")
