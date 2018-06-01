def count_positives(arr):
  count = 0
  for i in range(len(arr)):
    if arr[i] > 0:
      count+=1
      arr[-1] = count
  return arr

print(count_positives([1,55,43,22,1,23,3]))