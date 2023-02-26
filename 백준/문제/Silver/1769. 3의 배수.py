def solve(x):
    count = 0
    while True:
        if len(x) == 1:
            print(count)
            if int(x) % 3 == 0:
                print("YES")
            else:
                print("NO")
            return
        y = 0
        for num in x:
            y += int(num)
        count += 1
        x = str(y)

X = input()
solve(X)
