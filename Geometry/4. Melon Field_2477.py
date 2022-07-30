k = int(input())
arr_1 = []
arr_2 = []
for _ in range(6):
    line = list(map(int, input().split()))
    arr_1.append(line[0])
    arr_2.append(line[1])

i = 0
while i < 5 and not (arr_1.count(arr_1[i]) == 1 and arr_1.count(arr_1[i + 1]) == 1):
    arr_2.append(arr_2.pop(0))
    i += 1

area = arr_2[0] * arr_2[1] - arr_2[3] * arr_2[4]

print(area * k)
