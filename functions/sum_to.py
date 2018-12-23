def numbers():
    for i in range(1024):
        print(f"= {i}")
        yield i


def sum_to(n: int) -> int:
    sum: int = 0
    for i in numbers():
        if i == n: break
        sum += i
    return sum

print(sum_to(5))