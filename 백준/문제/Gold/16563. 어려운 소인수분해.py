def get_primes(size):
    primes = [i for i in range(size + 1)]
    for i in range(2, int(size**0.5) + 1):
        if primes[i] == i:
            for j in range(i * i, size + 1, i):
                primes[j] = min(primes[j], i)
    return primes


N = int(input())
numbers = list(map(int, input().split()))

primes = get_primes(max(numbers))

for number in numbers:
    res = []

    while number != 1:
        prime = primes[number]
        number //= prime
        res.append(prime)

    print(*res)
