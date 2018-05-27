def add_seven(arr):
  new_list = []
  for i in range(len(arr)):
    new_list.append(arr[i] + 7)
  return new_list
list1 = [1,2,3,4,5,6]
print(add_seven(list1))