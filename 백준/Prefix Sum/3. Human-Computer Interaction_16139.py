import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())

prefix_sum = [[0] * 26]

for i in range(len(s)):
    prefix_sum.append([element for element in prefix_sum[-1]])
    prefix_sum[-1][ord(s[i]) - 97] += 1

for i in range(q):
    alpha, l, r = input().split()
    l, r = int(l), int(r)
    res = prefix_sum[r + 1][ord(alpha) - 97] - prefix_sum[l][ord(alpha) - 97]
    print(res)
