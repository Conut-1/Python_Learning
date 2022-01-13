n = int(input())
count = 0

for num in range(1, n + 1):
    if num < 100:
        count += 1
    else:
        num_str = str(num)
        if int(num_str[0]) - int(num_str[1]) == int(num_str[1]) - int(num_str[2]):
            count += 1

print(count)