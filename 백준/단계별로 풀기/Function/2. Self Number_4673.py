import time
start = time.time()

a = list(range(1, 10_000 + 1))
b = []
for num in a:
    num_str = str(num)
    for i in num_str:
        num += int(i)
    if num <= 10_000:
        b.append(num)
for i in set(b):
    a.remove(i)
for i in a:
    print(i)

print("time : ", time.time() - start)