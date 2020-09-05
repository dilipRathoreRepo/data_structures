def sum_func(n):
    if int(n/10) == 0:
        return n
    return int(n % 10) + sum_func(int(n/10))


print(sum_func(32))
