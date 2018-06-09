def double_vision(arr):
  new_arr = []
  for i in range(len(arr)):
    new_arr.append(arr[i] * 2)
  return new_arr

arr = [1,2,3,4,5,6,7,8,9]

print(double_vision(arr))