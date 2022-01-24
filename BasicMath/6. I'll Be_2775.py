t = int(input())
for i in range(t):
    a = int(input())
    b = int(input())
    array = [[]]
    for i in range(1, b + 1):
        array[0].append(i)
    for i in range(1, a + 1):
        array.append([1])
        for j in range(1, b):
            array[i].append(array[i][j - 1] + array[i - 1][j])
    print(array[a][b - 1])