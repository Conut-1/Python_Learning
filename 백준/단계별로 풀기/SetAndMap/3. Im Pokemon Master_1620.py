import sys
input = sys.stdin.readline

n, m = map(int, input().split())
count = 1
dict_name = {}
dict_num = {}
for _ in range(n):
    name = input().strip()
    dict_name[name] = count
    dict_num[count] = name
    count += 1

for _ in range(m):
    target = input().strip()
    if target.isdigit():
        print(dict_num[int(target)])
    else:
        print(dict_name[target])
