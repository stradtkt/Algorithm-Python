def evens_and_odds(arr):
  for i in range(len(arr)):
    if arr[i] and arr[i+1] and arr[i+2]:
      if arr[i] % 2 == 0 and arr[i+1] % 2 == 0 and arr[i+2] % 2 == 0:
        print("Even more so!")

      if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
        print("That's odd!")

list1 = [1,5,2,4,6]
evens_and_odds(list1)