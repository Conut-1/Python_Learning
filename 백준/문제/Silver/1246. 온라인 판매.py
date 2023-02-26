import sys
input = sys.stdin.readline

N, M = map(int, input().split())
price = [int(input()) for _ in range(M)]

price.sort()
max_profit = 0
target_price = 0
for i in range(0 if M - N < 0 else M - N, M):
    if max_profit < price[i] * (M - i):
        max_profit = price[i] * (M - i)
        target_price = price[i]

print(target_price, max_profit)
