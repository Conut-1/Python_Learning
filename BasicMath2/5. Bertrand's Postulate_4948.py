arr = [False, False]
while True:
    n = int(input())
    if n == 0:
        break
    pre_step_len = len(arr)
    arr += [True] * (n * 2 + 1 - pre_step_len)
    cnt = 0
    for i in range(2, n * 2 + 1):
        if arr[i] == True:
            if n < i <= n * 2:
                cnt += 1
            if i > pre_step_len - 1:
                for j in range(2, (n * 2) // i + 1):
                    arr[i * j] = False
            else:
                for j in range((pre_step_len - 1) // i + 1, (n * 2) // i + 1):
                    arr[i * j] = False
    print(cnt)