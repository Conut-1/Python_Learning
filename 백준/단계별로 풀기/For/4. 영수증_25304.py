X = int(input())
N = int(input())
total_cost = 0
for i in range(N):
    cost, num = map(int, input().split())
    total_cost += cost * num

if X == total_cost:
    print("Yes")
else:
    print("No")
