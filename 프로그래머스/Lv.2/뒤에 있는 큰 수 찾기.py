def solution(numbers):
    answer = [-1] * (len(numbers))
    stack = []
    for i in range(len(numbers)):
        while stack and stack[-1] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer
