string = "abcd"


# OPTION !
# def reverse_string(s, output=None):
#     if output is None:
#         output = []
#     if s == '':
#         return ''.join(output)
#     output.append(s[len(s) - 1])
#     return reverse_string(s[:len(s) - 1], output)


# OPTION 2
def rev(s):
    if len(s) <= 1:
        return s
    return rev(s[1:]) + s[0]


# OPTION 3
# def reverse_string(s):
#     bag = []
#     output = []
#     for e in s:
#         bag.append(e)
#     i = 0
#     while i < len(s):
#         output.append(bag.pop())
#         i += 1
#     return ''.join(output)


print(rev(s=string))
