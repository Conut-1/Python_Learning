def gcf(a, b):
	while b:
		a, b = b, a % b
	return a

a, b = map(int, input().split())
c, d = map(int, input().split())
numerator = a * d + b * c
denominator = b * d

f = gcf(numerator, denominator)
print(numerator // f, denominator // f)
