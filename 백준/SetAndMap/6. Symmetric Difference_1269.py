n, m = map(int, input().split())
a = set(input().split())
b = input().split()

count = 0
for el in b:
    if el in a:
        count += 1
print(n + m - count * 2)
