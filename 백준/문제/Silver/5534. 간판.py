import sys
input = sys.stdin.readline

def match(old_idx, gap):
    for name_idx in range(len(name)):
        if old_idx + gap * name_idx >= len(old):
            return False
        if name[name_idx] != old[old_idx + gap * name_idx]:
            return False
    return True

N = int(input())
name = input().rstrip()
count = 0
for _ in range(N):
    old = input().rstrip()
    max_gap = (len(old) - 1) // (len(name) - 1)
    count_flag = False
    for gap in range(1, max_gap + 1):
        for i in range(len(old)):
            if match(i, gap):
                count += 1
                count_flag = True
                break
        if count_flag == True:
            break

print(count)
