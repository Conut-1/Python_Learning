n = int(input())
d = list(map(int, input().split()))
price = list(map(int, input().split()))

cur_price = price[0]
cost = 0
for i in range(n - 1):
    if cur_price > price[i]:
        cur_price = price[i]
    cost += cur_price * d[i]

print(cost)
