def solution(k, m, score):
    score.sort()
    answer = 0
    start = len(score) - m
    while start >= 0:
        answer += min(score[start:start + m]) * m
        start -= m
    return answer
