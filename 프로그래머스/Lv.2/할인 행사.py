def solution(want, number, discount):
    want_dict = dict()
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    answer = 0
    for i in range(len(discount)):
        if i >= 10:
            if discount[i - 10] in want_dict:
                want_dict[discount[i - 10]] += 1
                if want_dict[discount[i - 10]] == 0:
                    want_dict.pop(discount[i - 10])
            else:
                want_dict[discount[i - 10]] = 1

        if discount[i] in want_dict:
            want_dict[discount[i]] -= 1
            if want_dict[discount[i]] == 0:
                want_dict.pop(discount[i])
        else:
            want_dict[discount[i]] = -1

        if len(want_dict) == 0:
            answer += 1
    return answer
