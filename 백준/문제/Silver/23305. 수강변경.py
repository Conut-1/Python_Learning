N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dict = {}
for lecture in a:
    if lecture in dict:
        dict[lecture] += 1
    else:
        dict[lecture] = 1

res = 0
for lecture in b:
    if lecture in dict:
        if dict[lecture] == 0:
            res += 1
        else:
            dict[lecture] -= 1
    else:
        res += 1

print(res)
