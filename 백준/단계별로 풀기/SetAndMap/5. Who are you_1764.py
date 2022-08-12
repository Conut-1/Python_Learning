import sys
input = sys.stdin.readline

n, m = map(int, input().split())
no_hear = set(input().strip() for _ in range(n))

count = 0
result = []
for _ in range(m):
    str = input().strip()
    if str in no_hear:
        count += 1
        result.append(str)
result.sort()

print(count)
for str in result:
    print(str)
