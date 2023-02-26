M = int(input())
color_count = list(map(int, input().split()))
K = int(input())

percent = 0
for i in range(M):
	if color_count[i] < K:
		continue
	n = sum(color_count)
	cur_percent = 1
	for j in range(K):
		cur_percent *= (color_count[i] - j) / (n - j)
	percent += cur_percent

print(percent)
