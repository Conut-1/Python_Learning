def solution(book_time):
    answer = 0
    book_time.sort()
    used = [0] * len(book_time)
    count = 0
    while True:
        prev = "00:00"
        for i in range(len(book_time)):
            if used[i]:
                continue
            if prev <= book_time[i][0]:
                hour, min = map(int, book_time[i][1].split(':'))
                min += 10
                hour += min // 60
                min %= 60
                prev = ':'.join([str(hour).zfill(2), str(min).zfill(2)])
                used[i] = 1
                count += 1
        answer += 1
        if count == len(book_time):
            break
    return answer
