def GreatestCommonDivisor(a, b):
	while b > 0:
		if a > b:
			a = a - b
		else:
			b = b - a
	return a

print(GreatestCommonDivisor(52, 60))
