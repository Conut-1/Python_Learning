import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()
count = 0
i = 0
j = n - 1
while a[j] > x:
    j -= 1

while i < j:
    if a[i] + a[j] == x:
        count += 1
        i += 1
    elif a[i] + a[j] < x:
        i += 1
    else:
        j -= 1

print(count)
