input = list(map(int, input().split()))
res = 1
while True:
    count = 0
    for i in input:
        if res % i == 0:
            count += 1
    if count >= 3:
        break
    res += 1
print(res)
