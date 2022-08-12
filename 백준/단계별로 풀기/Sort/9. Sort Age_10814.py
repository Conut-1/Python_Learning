import sys
input = sys.stdin.readline

n = int(input())
arr = [input().split() for _ in range(n)]

dict = {}
for age, name in arr:
    age = int(age)
    if age in dict:
        dict[age].append(name)
    else:
        dict[age] = [name]

key = sorted(dict.keys())
for k in key:
    name_arr = dict[k]
    for name in name_arr:
        print(k, name)
