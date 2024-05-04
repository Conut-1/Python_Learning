n = int(input())
parents = list(map(int, input().split()))
target = int(input())

root = -1
tree = [[] for _ in range(n)]
for i, parent in enumerate(parents):
    if parent == -1:
        root = i
    elif i != target:
        tree[parent].append(i)

count = 0
stack = []
if target != root:
    stack.append(root)

while stack:
    cur = stack.pop()
    if not tree[cur]:
        count += 1
        continue
    stack.extend(tree[cur])

print(count)
