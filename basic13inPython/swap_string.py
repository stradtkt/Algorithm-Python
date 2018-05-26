def swap_string(arr):
  for i in range(len(arr)):
    if arr[i] < 0:
      arr[i] = "Dojo"
  return arr
list1 = [-1,-2,-3,-4,1,2,3,4]
print(swap_string(list1))