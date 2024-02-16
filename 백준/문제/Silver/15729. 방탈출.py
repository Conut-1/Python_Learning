n = int(input())
numbers = list(map(int, input().split()))

lamps = [0] * n
count = 0
for i in range(n):
    if numbers[i] != lamps[i]:
        numbers[i] = 1 if numbers[i] == 0 else 0
        if i + 1 < n:
            numbers[i + 1] = 1 if numbers[i + 1] == 0 else 0
        if i + 2 < n:
            numbers[i + 2] = 1 if numbers[i + 2] == 0 else 0
        count += 1

print(count)
