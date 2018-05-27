def fibonacci(num):
  sums = 1
  i = 0
  j = 1
  while num > 1:
    sums = i + j
    i = j
    j = sums
    num-=1
  return sums

print(fibonacci(4))