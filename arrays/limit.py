def limit(arr, min_limit=None, max_limit=None):
    result = []
    if min_limit == None:
        for i in arr:
            if i <= max_limit:
                result.append(i)
    elif max_limit == None:
        for i in arr:
            if i >= min_limit:
                result.append(i)
    else:
        for i in arr:
            if i >= min_limit and i <= max_limit:
                result.append(i)
    print(result)
    return result


if __name__ == '__main__':
    limit([1,2,3,3,4,5,6,65,43,23,43,23,43,212,43], 43, 212)

    # [65, 43, 43, 43, 212, 43]