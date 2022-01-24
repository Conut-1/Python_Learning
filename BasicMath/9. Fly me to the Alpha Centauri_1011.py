import math
t = int(input())
"""
for i in range(t):
    x, y = map(int, input().split())
    difference = y - x
    sum = 0
    i = 2
    while True:
        if(difference <= sum + i // 2):
            print(i - 1)
            break
        sum += i // 2
        i += 1
"""
for i in range(t):
    x, y = map(int, input().split())
    difference = y - x
    a = math.floor(math.sqrt(difference))
    if(difference == a ** 2):
        print(a * 2 - 1)
    elif(difference <= a ** 2 + a ):
        print(a * 2)
    else:
        print(a * 2 + 1)