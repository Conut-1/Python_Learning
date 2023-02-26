def is_clock_num(num):
    card = list(str(num))
    for _ in range(4):
        if num > int(''.join(card)):
            return False
        card = card[1:] + [card[0]]
    return True

card = input().split()

arr = []
for i in range(4):
    arr.append(int(''.join(card)))
    card = card[1:] + [card[0]]
arr.sort()

clock_num = arr[0]

count = 0
for num in range(1111, 10000):
    if not is_clock_num(num):
        continue
    count += 1
    if num == clock_num:
        break

print(count)
