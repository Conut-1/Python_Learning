import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


preorder = []
while True:
    try:
        num = int(input())
        preorder.append(num)
    except:
        break


def postorder(first, end):
    if first > end:
        return
    mid = end + 1
    for i in range(first + 1, end + 1):
        if preorder[first] < preorder[i]:
            mid = i
            break
    
    postorder(first + 1, mid - 1)
    postorder(mid, end)
    print(preorder[first])


postorder(0, len(preorder) - 1)
