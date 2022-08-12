import sys
input = sys.stdin.readline


def division(k, x, y):
    global minus
    global zero
    global plus

    flag = False
    if arr[x][y] == "-1":
        for i in range(k * k):
            if arr[x + i // k][y + i % k] != "-1":
                flag = True
                break
    elif arr[x][y] == "0":
        for i in range(k * k):
            if arr[x + i // k][y + i % k] != "0":
                flag = True
                break
    elif arr[x][y] == "1":
        for i in range(k * k):
            if arr[x + i // k][y + i % k] != "1":
                flag = True
                break
    if flag:
        division(k // 3, x, y)
        division(k // 3, x, y + k // 3)
        division(k // 3, x, y + k // 3 * 2)
        division(k // 3, x + k // 3, y)
        division(k // 3, x + k // 3, y + k // 3)
        division(k // 3, x + k // 3, y + k // 3 * 2)
        division(k // 3, x + k // 3 * 2, y)
        division(k // 3, x + k // 3 * 2, y + k // 3)
        division(k // 3, x + k // 3 * 2, y + k // 3 * 2)
    else:
        if arr[x][y] == "-1":
            minus += 1
        elif arr[x][y] == "0":
            zero += 1
        elif arr[x][y] == "1":
            plus += 1


n = int(input())
arr = [input().split() for _ in range(n)]

minus = 0
zero = 0
plus = 0
division(n, 0, 0)

print(minus)
print(zero)
print(plus)
