import sys
sys.stdin.readline


n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

count = 0
for el in coin[::-1]:
    count += k // el
    k %= el
    if k == 0:
        break

print(count)
