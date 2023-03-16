def solution(topping):
    from collections import Counter

    one = set()
    two = Counter(topping)

    answer = 0
    for t in topping:
        two[t] -= 1
        if two[t] == 0:
            two.pop(t)

        one.add(t)

        if len(one) == len(two):
            answer += 1

    return answer
