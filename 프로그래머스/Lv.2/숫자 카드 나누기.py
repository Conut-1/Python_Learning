def solution(arrayA, arrayB):
	def gcd(a, b):
		while b:
			a, b = b, a % b
		return a

	gcd_a = arrayA[0]
	for i in arrayA[1:]:
		gcd_a = gcd(gcd_a, i)
	gcd_b = arrayB[0]
	for i in arrayB[1:]:
		gcd_b = gcd(gcd_b, i)

	for a in arrayA:
		if a % gcd_b == 0:
			gcd_b = 0
			break
	for b in arrayB:
		if b % gcd_a == 0:
			gcd_a = 0
			break

	answer = max(gcd_a, gcd_b)
	return answer
