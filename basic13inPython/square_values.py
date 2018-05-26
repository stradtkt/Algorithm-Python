def square_values(arr):
  for i in range(len(arr)):
    arr[i] *= arr[i]
  return arr

list1 = [1,2,3,4,5,6,7]
print(square_values(list1))