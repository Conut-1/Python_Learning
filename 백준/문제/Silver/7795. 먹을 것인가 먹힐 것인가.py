import sys
input = sys.stdin.readline

def search(creature):
	start = 0
	end = m - 1
	while start <= end:
		mid = (start + end) // 2
		if creature > b[mid]:
			start = mid + 1
		else:
			end = mid - 1
	return end + 1

T = int(input())
for _ in range(T):
	n, m = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))

	b.sort()
	count = 0
	for creature in a:
		count += search(creature)

	print(count)
