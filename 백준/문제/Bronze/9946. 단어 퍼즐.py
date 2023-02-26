import sys
input = sys.stdin.readline

i = 0
while True:
    i += 1
    same = True
    prev = input().strip()
    cur = input().strip()
    for chr in prev:
        if cur.count(chr) != prev.count(chr):
            same = False
            break
    if prev == "END" and cur == "END":
        break
    print(f"Case {i}:", "same" if same == True else "different")
