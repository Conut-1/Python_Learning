def solution(n, m, section):
    answer = 0
    while section:
        start = section.pop()
        while section and section[-1] > start - m:
            section.pop()
        answer += 1
    return answer
