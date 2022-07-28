str = input()
set = set()

for i in range(1, len(str) + 1):
    for j in range(len(str) - i + 1):
        set.add(str[j:j + i])
print(len(set))
