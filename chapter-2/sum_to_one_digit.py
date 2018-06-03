def sum_to_one(num):
	if num < 10:
		return num
	string = str(num)
	sums = 0
	for i in range(len(string)):
		sums += int(string[i])
	return sum_to_one(sums)
print(sum_to_one(123456789))
# 9