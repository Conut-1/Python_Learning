# num = int(input())
# factor = list(map(int, input().split()))

# result = max(factor) * min(factor)

# print(result)

num = int(input())
factor = list(map(int, input().split()))

result = 2 * max(factor)
while True:
    correct = 1
    for el in factor:
        if result % el != 0:
            correct = 0
            break
    if correct == 1:
        break
    result += 1
if len(factor) == 1:
    result = factor[0] ** 2

print(result)
