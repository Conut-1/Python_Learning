n, m = map(int, input().split())

if n > m:
    a = m
else:
    a = n
lcm = 1
for i in range(1, a + 1):
    if n % i == 0 and m % i == 0:
        lcm = i
gcf = n * m // lcm

print(lcm)
print(gcf)
