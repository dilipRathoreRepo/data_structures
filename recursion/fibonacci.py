# OPTION 1
# def fib(n, output=None):
#     if n < 2:
#         return 0
#     if output is None:
#         a = 0
#         b = 1
#         output = [a, b]
#     if len(output) <= n:
#         c = output[-1] + output[-2]
#         output.append(c)
#         fib(n, output)
#     return output


# OPTION 2 : running iteratively in loop
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a


# OPTION 3 : using recursion
# def fib(n):
#     if n == 0  or n == 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(10))


# OPTION 4: using memoization and recursion
n = 10
cache = [None] * (n+1)


def fib_memo_rec(n):
    # Base Case
    if n == 0 or n == 1:
        return n

    # Check Cache
    if cache[n] is not None:
        return cache[n]

    # Keep setting cache
    cache[n] = fib_memo_rec(n-1) + fib_memo_rec(n-2)
    return cache[n]


print(fib_memo_rec(10))

# fib(7) = [0,1,1,2,3,5,8]
# fib(8) = [0,1,1,2,3,5,8,13, 21, 34, 55, 89]




