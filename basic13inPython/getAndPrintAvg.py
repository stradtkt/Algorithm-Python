def print_average(arr):
  sums = 0
  avg = 0
  for i in range(len(arr)):
    sums += i
  avg = sums/len(arr)
  return avg
list1 = [1,2,3,4,5,6,7]
print(print_average(list1))