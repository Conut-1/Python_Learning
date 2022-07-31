import sys
input = sys.stdin.readline

input_value = input().strip()
count = 0

if len(input_value) == 1:
    input_value = "0" + input_value

b = input_value

while True:
    a = str(int(b[0]) + int(b[1]))
    b = b[1] + a[-1]
    count += 1
    if b == input_value:
        print(count)
        break