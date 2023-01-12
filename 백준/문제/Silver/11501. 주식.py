import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    stocks = list(map(int, input().split()))

    cur_max = 0
    profit = 0
    for i in range(n - 1, -1, -1):
        if stocks[i] > cur_max:
            cur_max = stocks[i]
        else:
            profit += (cur_max - stocks[i])

    print(profit)
