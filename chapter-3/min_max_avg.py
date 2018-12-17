def min_max_avg(arr):
    the_min = min(arr)
    the_max = max(arr)
    the_sum = 0
    for i in range(len(arr)):
        the_sum += arr[i]
    the_avg = the_sum / len(arr)
    print("MIN:", the_min)
    print("MAX:", the_max)
    print("SUM:", the_sum)
    print("AVG:", the_avg)

min_max_avg([1,2,3,4,5,6,6,7,8,9,34,23,43,4,32,3423,2,2,223344])

