import sys
input = sys.stdin.readline

def quadtree(k, x, y):
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
        return f"({quadtree(k // 2, x, y)}{quadtree(k // 2, x, y + k // 2)}{quadtree(k // 2, x + k // 2, y)}{quadtree(k // 2, x + k // 2, y + k // 2)})"
    else:
        if arr[x][y] == "1":
            return "1"
        elif arr[x][y] == "0":
            return "0"


n = int(input())
arr = [input().rstrip() for _ in range(n)]

print(quadtree(n, 0, 0))
