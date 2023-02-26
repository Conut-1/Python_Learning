def solution(food):
    answer = '0'
    for i in range(len(food) - 1, -1, -1):
        while food[i] > 1:
            food[i] -= 2
            answer = str(i) + answer + str(i)
    return answer
