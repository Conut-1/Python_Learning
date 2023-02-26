import sys
input = sys.stdin.readline

N = int(input())

extension = dict()
for _ in range(N):
    filename = input().rstrip().split('.')
    if filename[1] in extension:
        extension[filename[1]] += 1
    else:
        extension[filename[1]] = 1

res = sorted(list(extension.items()))
for el in res:
    print(*el)
