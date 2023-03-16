import sys

input = sys.stdin.readline

N = int(input())

words = dict()
for _ in range(N):
    word = input().rstrip()

    alpha = [0] * 26
    shom = ""
    count = 0
    for cha in word:
        if alpha[ord(cha) - ord("a")] == 0:
            count += 1
            alpha[ord(cha) - ord("a")] = count
        shom += str(alpha[ord(cha) - ord("a")])

    if shom in words:
        words[shom] += 1
    else:
        words[shom] = 1

res = 0
for value in words.values():
    res += value * (value - 1) // 2
print(res)
