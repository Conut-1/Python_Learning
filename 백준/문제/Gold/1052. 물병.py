n, k = map(int, input().split())

n_bin = bin(n)
start = 2
count = 0
while count < k and start < len(n_bin):
    if n_bin[start] == "1":
        count += 1
    start += 1

res = 0
if start != len(n_bin):
    remain = int(n_bin[start:], 2)
    if remain != 0:
        res = 2 ** (len(n_bin) - start) - remain

print(res)
