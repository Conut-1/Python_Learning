budget = int(input())
prices = list(map(int, input().split()))

j_budget = s_budget = budget
j_stock = 0
s_stock = 0
up_count = 0
down_count = 0
for i in range(len(prices)):
    j_buy = j_budget // prices[i]
    j_budget -= j_buy * prices[i]
    j_stock += j_buy

    if i > 0:
        if prices[i] > prices[i - 1]:
            up_count += 1
            down_count = 0
        elif prices[i] == prices[i - 1]:
            up_count = 0
            down_count = 0
        else:
            up_count = 0
            down_count += 1
    if up_count >= 3:
        s_budget += s_stock * prices[i]
        s_stock = 0
    if down_count >= 3:
        s_buy = s_budget // prices[i]
        s_budget -= s_buy * prices[i]
        s_stock += s_buy

if j_budget + j_stock * prices[-1] > s_budget + s_stock * prices[-1]:
    print("BNP")
elif j_budget + j_stock * prices[-1] < s_budget + s_stock * prices[-1]:
    print("TIMING")
else:
    print("SAMESAME")
