import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

dict = {}
for word in arr:
    length = len(word)
    if length in dict:
        dict[length].add(word)
    else:
        dict[length] = set([word])

key = sorted(dict.keys())
for k in key:
    word = sorted(list(dict[k]))
    for w in word:
        print(w)
