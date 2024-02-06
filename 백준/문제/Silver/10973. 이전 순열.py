n = int(input())
seq = list(map(int, input().split()))

i = len(seq) - 1

while i > 0:
    if seq[i - 1] > seq[i]:
        break
    i -= 1

if i == 0:
    print(-1)
else:
    res = seq[: i - 1]
    arr = seq[i - 1 :]
    target = max([e for e in arr if e < arr[0]])
    res.append(target)
    arr.remove(target)
    arr.sort(reverse=True)
    res += arr
    print(" ".join(map(str, res)))
