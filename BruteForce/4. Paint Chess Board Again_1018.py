result = 64
n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        count = 0
        color = "W"
        if lst[i][j] == "W":
            color = "B"
        for k in range(8):
            if color == "B":
                color = "W"
            elif color == "W":
                color = "B"
            for l in range(8):
                if lst[i + k][j + l] == "B" and color == "B":
                    color = "W"
                elif lst[i + k][j + l] == "W" and color == "W":
                    color = "B"
                elif color == "B":
                    count += 1
                    color = "W"
                else:
                    count += 1
                    color = "B"
        if count == 0:
            result = count
            exit
        if count > 32:
            count = 64 - count
        if result > count:
            result = count
print(result)
