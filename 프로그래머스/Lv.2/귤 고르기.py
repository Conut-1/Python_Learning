def solution(k, tangerine):
	tangerine_dict = dict()
	for t in tangerine:
		if t in tangerine_dict:
			tangerine_dict[t] += 1
		else:
			tangerine_dict[t] = 1
	sorted_tangerine = sorted(tangerine_dict.items(), key=lambda x: x[1])
	answer = 0
	sum = 0
	for size, num in sorted_tangerine[::-1]:
		sum += num
		answer += 1
		if sum >= k:
			break
	return answer
