M = 1234567891
r = 31

def sqrt(r, i):
    res = 1
    for _ in range(i):
        res = res * r % M

    return res

L = int(input())
string = input()

sum = 0
for i in range(len(string)):
    sum = (sum + (ord(string[i]) - ord("a") + 1) * sqrt(r, i)) % M

print(sum % M)
