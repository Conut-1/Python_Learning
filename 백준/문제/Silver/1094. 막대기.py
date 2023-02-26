X = int(input())

count = 0
size = 64
while size:
    if X & size:
        count += 1
    size >>= 1

print(count)
