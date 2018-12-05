def binary_search(arr, query):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        val = arr[mid]
        if val == query:
            return mid
        elif val < query:
            low = mid + 1
        else:
            high = mid - 1
    return None