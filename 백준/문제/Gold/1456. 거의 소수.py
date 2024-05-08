m, n = map(int, input().split())

prime = [True] * (int(n**0.5) + 1)
for i in range(2, int(n**0.5) + 1):
    if prime[i]:
        if i * i > int(n**0.5):
            break
        for j in range(i**2, int(n**0.5) + 1, i):
            prime[j] = False

count = 0
for i in range(2, len(prime)):
    if not prime[i]:
        continue
    near_prime = i
    while True:
        near_prime *= i
        if near_prime < m:
            continue
        if near_prime > n:
            break
        count += 1

print(count)
