n = int(input())
num_5 = 0
num_3 = 0

for i in range(n // 5, -1, -1):
    num_5 = i
    num_3 = (n - 5 * i) // 3
    if((n - 5 * i) % 3 == 0):
        break
    if(i == 0):
        num_5 = 0
        num_3 = -1

print(num_5 + num_3)