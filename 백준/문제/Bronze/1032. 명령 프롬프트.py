N = int(input())
pattern = list(input())
for _ in range(N - 1):
    file = input()
    for i in range(len(pattern)):
        if pattern[i] != '?' and pattern[i] != file[i]:
            pattern[i] = '?'

print(('').join(pattern))
