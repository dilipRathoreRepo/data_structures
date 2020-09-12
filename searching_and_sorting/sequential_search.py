# import collections

unsorted_list = [-199, 1, 4, 2, 6, -900, 3]
sorted_list = [0, 1, 3, 5, 9, 14]


def minimum(lst):
    min_val = lst[0]
    for e in lst[1:]:
        if e < min_val:
            min_val = e
    return min_val


def sort_it(lst):
    sorted_lst = []
    while len(lst) > 0:
        min_item = minimum(lst)
        sorted_lst.append(min_item)
        lst.remove(min_item)
    return sorted_lst


print(sort_it(unsorted_list))


def unsorted_seq_search(arr, ele):
    for e in arr:
        if e == ele:
            return True
    return False


def sorted_seq_search(arr, ele):
    for e in arr:
        if e == ele:
            return True
        elif e > ele:
            return False
    return False


print(unsorted_seq_search(unsorted_list, 4))
print(sorted_seq_search(sorted_list, -1))
