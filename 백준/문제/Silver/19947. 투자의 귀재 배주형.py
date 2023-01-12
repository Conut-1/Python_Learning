def plan(money, year, rate):
    global max_profit

    money = int(money * rate)
    max_profit = max(max_profit, money)
    solve(money, year)

def solve(money, year):
    if Y - year >= 1:
        plan(money, year + 1, 1.05)
    if Y - year >= 3:
        plan(money, year + 3, 1.20)
    if Y - year >= 5:
        plan(money, year + 5, 1.35)

H, Y = map(int, input().split())

max_profit = 0
solve(H, 0)

print(max_profit)
