def solution(s):
    pos = {}
    answer = []
    for i in range(len(s)):
        if s[i] not in pos:
            answer.append(-1)
        else:
            answer.append(i - pos[s[i]])
        pos[s[i]] = i
    return answer
