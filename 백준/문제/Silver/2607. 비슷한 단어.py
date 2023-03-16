import sys

sys.stdin.readline

N = int(input())
first = input().rstrip()

first_arr = [0] * 26
for cha in first:
    first_arr[ord(cha) - ord("A")] += 1

count = 0
for _ in range(N - 1):
    word = input().rstrip()

    word_arr = [0] * 26
    for cha in word:
        word_arr[ord(cha) - ord("A")] += 1

    diff = ""
    for i in range(26):
        diff += abs(first_arr[i] - word_arr[i]) * chr(i + ord("A"))

    if abs(len(first) - len(word)) <= 1:
        if len(diff) <= 1:
            count += 1
        elif len(diff) == 2 and diff[0] != diff[1]:
            count += 1

print(count)
