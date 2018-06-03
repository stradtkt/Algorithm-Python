import math
def most_significant_digit(num):
	num = abs(num)
	if num < 1:
		while num < 10:
			num *= 10
			if num > 1 and num < 10:
				return math.floor(num)
	elif num > 10:
		while num > 10:
			num /= 10
			if num > 1 and num < 10:
				return math.trunc(num)

print(most_significant_digit(123456))
# 1
print(most_significant_digit(999999999))
# 9