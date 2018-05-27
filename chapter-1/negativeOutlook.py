def negativeOutlook(arr):
  new_list = []
  for i in range(len(arr)):
    if arr[i] > 0:
      new_list.append(arr[i] - arr[i] * 2)
    elif arr[i] < 0:
      new_list.append(arr[i])
  return new_list

list1 = [-1,-2,1,3,5]
print(negativeOutlook(list1))