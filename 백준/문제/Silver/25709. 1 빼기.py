n = int(input())

count = 0
while n:
    if n != 1 and '1' in str(n):
        n = int(str(n).replace('1', '', 1))
        count += 1
    else:
        n -= 1
        count += 1

print(count)
