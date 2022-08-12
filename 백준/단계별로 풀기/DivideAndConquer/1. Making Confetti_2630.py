import sys
input = sys.stdin.readline

def quadtree(k, x, y):
    global blue
    global white

    flag = False
    if arr[x][y] == "1":
        for i in range(k * k):
            if arr[x + i // k][y + i % k] == "0":
                flag = True
                break
    elif arr[x][y] == "0":
        for i in range(k * k):
            if arr[x + i // k][y + i % k] == "1":
                flag = True
                break
    if flag:
        quadtree(k // 2, x, y)
        quadtree(k // 2, x, y + k // 2)
        quadtree(k // 2, x + k // 2, y)
        quadtree(k // 2, x + k // 2, y + k // 2)
    else:
        if arr[x][y] == "1":
            blue += 1
        elif arr[x][y] == "0":
            white += 1


n = int(input())
arr = [input().split() for _ in range(n)]

blue = 0
white = 0
quadtree(n, 0, 0)

print(white)
print(blue)
