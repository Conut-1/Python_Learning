test_case = int(input())

for i in range(test_case):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]
    count = 0
    for score in arr[1:]:
        if score > avg:
            count += 1
    result = count / arr[0]
    print("{:.3f}%".format(result * 100))