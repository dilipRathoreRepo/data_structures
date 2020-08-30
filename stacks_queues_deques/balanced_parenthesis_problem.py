from stacks_queues_deques.stacks import Stack
# import collections


# def balance_check(string):
#     """
#     Checks if all the parenthesis are properly closed in a string
#     :param string:
#     :return: Boolean
#     """
#     lookup = {"[": "]", "(": ")", "{": "}"}
#
#     length = len(string)
#     if length % 2 != 0:
#         return False
#     mid_point = int(length/2)
#     first_half_elements = []
#     second_half_elements = []
#
#     for item in string[0:mid_point]:
#         first_half_elements.append(item)
#
#     for item in string[mid_point:]:
#         second_half_elements.append(item)
#
#     converted = []
#     for item in reversed(first_half_elements):
#         converted.append(lookup[item])
#     return second_half_elements == converted


def balance_check(string):
    opening = set('[{(')
    matches = {('[', ']'), ('{', '}'), ('(', ')')}

    if len(string) % 2 != 0:
        return False

    stack = []
    for e in string:
        if e in opening:
            stack.append(e)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, e) not in matches:
                return False
    if len(stack) != 0:
        return False
    return True


string = "[{{{(())}}}]((()))"
print(balance_check(string))
