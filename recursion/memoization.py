# output = {}
#
#
# def factorial(n):
#     if n == 0:
#         return 1
#     if n not in output:
#         output[n] = factorial(n - 1) * n
#         return output[n]
#
#
# print(factorial(4))
# print(output)


def simple_factorial(n):
    if n < 2:
        return 1
    return n * simple_factorial(n - 1)


class Memoization:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.f(args)
        return self.memo[args]


mem = Memoization(simple_factorial)
print(mem(4))
