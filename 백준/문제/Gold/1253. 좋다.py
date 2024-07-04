N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

count = 0
for i in range(N):
    goal = numbers[i]
    start = 0
    end = len(numbers) - 1
    while start < end:
        if numbers[start] + numbers[end] == goal:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                count += 1
                break
        elif numbers[start] + numbers[end] > goal:
            end -= 1
        elif numbers[start] + numbers[end] < goal:
            start += 1

print(count)
