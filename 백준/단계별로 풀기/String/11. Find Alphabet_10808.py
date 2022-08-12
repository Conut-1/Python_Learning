"""
s = input()
count = {}
for item in s:
    try:
        count[item] += 1
    except:
        count[item] = 1

arr = []
for alp in range(ord('a'), ord('z') + 1):
    try:
        arr.append(count[chr(alp)])
    except:
        arr.append(0)
print(*arr)
"""
s = input()
arr = [0] * 26
for item in s:
    arr[ord(item) - ord('a')] += 1
print(*arr)