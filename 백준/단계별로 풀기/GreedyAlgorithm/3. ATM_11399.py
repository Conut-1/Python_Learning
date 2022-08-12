n = int(input())
p = list(map(int, input().split()))

p.sort()
time = 0
sum = 0
for el in p:
    time += el
    sum += time

print(sum)
