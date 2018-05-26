def arrayWithOdds(arr):
  new_list = []
  for i in range(1, 255):
    if i % 2 != 0:
      new_list.append(i)
  return new_list

list1 = [1,2,3,4,5,6,7,8,9]
print(arrayWithOdds(list1))