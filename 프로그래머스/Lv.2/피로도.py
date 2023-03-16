def solution(k, dungeons):
    from itertools import permutations

    answer = 0
    for p in permutations(range(len(dungeons)), len(dungeons)):
        count = 0
        fatigue = k
        for i in p:
            if fatigue >= dungeons[i][0]:
                fatigue -= dungeons[i][1]
                count += 1
        answer = max(answer, count)
    return answer
