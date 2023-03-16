import sys

lines = sys.stdin.readlines()

tree_dict = dict()
count = 0
for line in lines:
    tree = line.rstrip("\n")

    if tree in tree_dict:
        tree_dict[tree] += 1
    else:
        tree_dict[tree] = 1
    count += 1

for tree in sorted(tree_dict.keys()):
    print(f"{tree} {tree_dict[tree] * 100 / count:.4f}")
