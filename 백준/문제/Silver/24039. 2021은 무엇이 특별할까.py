N = int(input())
arr = [True] * (10_000 + 1)
arr[0] = False
arr[1] = False

prime = []
for i in range(2, 10_000 + 1):
    if arr[i] == True:
        prime.append(i)
        for j in range(2, 10_000 // i + 1):
            arr[i * j] = False

for i in range(len(prime) - 1):
    if prime[i] * prime[i + 1] > N:
        print(prime[i] * prime[i + 1])
        break
