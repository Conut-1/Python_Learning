input_value = input().split()
a = input_value[0][::-1]
b = input_value[1][::-1]
if int(a) > int(b):
    print(a)
else:
    print(b)