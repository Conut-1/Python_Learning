import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    dict = {}
    for __ in range(n):
        name, part = input().split()
        if part in dict:
            dict[part] += 1
        else:
            dict[part] = 1

    result = 1
    for part in dict.keys():
        result *= dict[part] + 1

    print(result - 1)
