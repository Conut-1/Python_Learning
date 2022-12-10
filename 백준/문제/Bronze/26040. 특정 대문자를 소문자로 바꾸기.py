string = input()
for upper in input().split():
    string = string.replace(upper, upper.lower())
print(string)
