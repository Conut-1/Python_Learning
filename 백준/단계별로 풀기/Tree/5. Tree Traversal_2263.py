import sys
sys.setrecursionlimit(1000000)

def find_tree(start, end, postorder_index):
    if start > end or postorder_index < 0:
        return
    root = postorder[postorder_index]
    print(root, end=' ')
    root_index = position[postorder[postorder_index]]
    find_tree(start, root_index - 1, postorder_index - 1 - (end - root_index))
    find_tree(root_index + 1, end, postorder_index - 1)


N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0] * (N + 1)
for i in range(N):
    position[inorder[i]] = i
find_tree(0, N - 1, N - 1)
