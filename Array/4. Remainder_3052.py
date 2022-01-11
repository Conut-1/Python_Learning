count = 0
arr = []
for i in range(10):
    a = int(input())
    a %= 42
    if not a in arr:
        arr.append(a)

print(len(arr))