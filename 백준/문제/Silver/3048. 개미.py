N1, N2 = map(int, input().split())
ant1 = input()
ant2 = input()
T = int(input())

res = ""
count = len(ant1) - T
i = 0
j = 0
while i < len(ant1) or j < len(ant2):
    if count > 0 and i < len(ant1):
        res += ant1[-1 - i]
        i += 1
        count -= 1
    elif j < len(ant2):
        res += ant2[j]
        j += 1
        count += 1
    else:
        count += 1
print(res)
