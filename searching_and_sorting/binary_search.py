lst = [1, 3, 5, 6, 7, 10, 28]


# OPTION 1
# def binary_search(sorted_list, ele):
#     while len(sorted_list) > 0:
#         mid_point = len(sorted_list) // 2
#         if ele == sorted_list[mid_point]:
#             return True
#         elif ele > sorted_list[mid_point]:
#             sorted_list = sorted_list[mid_point+1:]
#         else:
#             sorted_list = sorted_list[: mid_point]
#     return False

# OPTION 2
def binary_search(sorted_list, ele):
    if len(sorted_list) == 0:
        return False
    else:
        mid_point = len(sorted_list) // 2
        if ele == sorted_list[mid_point]:
            return True
        elif ele > sorted_list[mid_point]:
            return binary_search(sorted_list[mid_point+1:], ele)
        else:
            return binary_search(sorted_list[: mid_point], ele)


print(binary_search(lst, -128))
