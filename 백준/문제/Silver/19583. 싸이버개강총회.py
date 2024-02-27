import sys

input = sys.stdin.readline

s, e, q = input().split()

check_set = set()
count = 0
while True:
    try:
        time_log, nickname = input().split()
        if time_log <= s:
            check_set.add(nickname)
        elif e <= time_log <= q and nickname in check_set:
            check_set.discard(nickname)
            count += 1
    except:
        break

print(count)
