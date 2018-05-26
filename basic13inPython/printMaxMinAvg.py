def max_min_avg(arr):
  maxs = 0
  mins = 0
  sums = 0
  avg = 0
  for i in range(len(arr)):
    if arr[i] > maxs:
      maxs = i
    if i < mins:
      mins = i
    sums += i
  avg = sums / len(arr)
  print("Min is: " + str(arr[mins]) + " Max is: " + str(arr[maxs]) + " Average is: " + str(avg))

list1 = [1,2,3,4,5,6,7,8]
max_min_avg(list1)