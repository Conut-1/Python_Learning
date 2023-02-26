def solution(k, score):
    answer = []
    fame = []
    for s in score:
        for i in range(k):
            if i >= len(fame):
                fame.append(s)
                break
            if s >= fame[i]:
                fame[i], s = s, fame[i]
        answer.append(fame[-1])
    return answer
