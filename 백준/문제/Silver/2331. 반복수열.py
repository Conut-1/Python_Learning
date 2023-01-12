A, P = map(int, input().split())

d_set = set([A])
d_arr = [A]
cur = A
while True:
    new = 0
    for digit in str(cur):
        new += int(digit) ** P
    if new in d_set:
        print(d_arr.index(new))
        break
    else:
        d_set.add(new)
        d_arr.append(new)
        cur = new
