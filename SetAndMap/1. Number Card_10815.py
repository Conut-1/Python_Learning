input()
card = list(map(int, input().split()))
input()
guess = list(map(int, input().split()))
result = []

dict = {}
for num in card:
    dict[num] = 1

for num in guess:
    if num in dict:
        result.append(1)
    else:
        result.append(0)

print(" ".join(map(str, result)))
