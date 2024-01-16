import sys

input = sys.stdin.readline
n = int(input())
count = 0

chat_set = set()
for _ in range(n):
    log = input().strip()
    if log == "ENTER":
        count += len(chat_set)
        chat_set.clear()
    else:
        chat_set.add(log)
count += len(chat_set)

print(count)
