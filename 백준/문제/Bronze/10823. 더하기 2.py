import sys
input = sys.stdin.readline

s = ''
while True:
    string = input().strip()
    if not string:
        break
    s += string

res = sum(map(int, s.split(',')))

print(res)
