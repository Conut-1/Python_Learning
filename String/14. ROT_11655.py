input_value = input()
result = ''
for i in input_value:
    if i.isalpha():
        if ord('a') <= ord(i) <= ord('m') or ord('A') <= ord(i) <= ord('M'):
            result += chr(ord(i) + 13)
        else:
            result += chr(ord(i) - 13)
    else:
        result += i
print(result)