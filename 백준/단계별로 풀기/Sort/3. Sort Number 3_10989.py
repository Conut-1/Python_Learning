import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10001
for i in range(n):
    count[int(input())] += 1

for num in range(10001):
    if count[num] != 0:
        for i in range(count[num]):
            print(num)
