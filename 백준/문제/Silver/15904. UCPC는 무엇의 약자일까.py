string = input()
res = ''
count = 0
stack = ['C', 'P', 'C', 'U']
for chr in string:
    if count == 4:
        break
    if stack[-1] == chr:
        stack.pop()
        count += 1

if count == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')
