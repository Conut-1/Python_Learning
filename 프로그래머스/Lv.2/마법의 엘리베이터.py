def solution(storey):
    answer = 0
    while storey:
        if storey % 10 < 5:
            answer += storey % 10
        elif storey % 10 == 5:
            if storey % 100 // 10 > 4:
                storey += 5
            answer += 5
        else:
            answer += 10 - storey % 10
            storey += 10 - storey % 10
        storey //= 10
    return answer
