n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input())
check = [input() for _ in range(m)]

count = 0
for str in check:
    if str in s:
        count += 1

print(count)