lst = [110, 11, 1, 3]


# OPTION 1
def bubble_sort(input_list):
    total_checks = 0
    for k in range(len(input_list)-1):
        i = 0
        while i < len(input_list) - 1:
            if input_list[i] > input_list[i+1]:
                tmp = input_list[i+1]
                input_list[i + 1] = input_list[i]
                input_list[i] = tmp
            i += 1
            total_checks += 1
    return total_checks, input_list


# OPTION 2
def bubble_sort_2(input_list):
    total_checks = 0
    for n in range(len(input_list)-1, 0, -1):
        for k in range(n):
            if input_list[k] > input_list[k+1]:
                temp = input_list[k+1]
                input_list[k+1] = input_list[k]
                input_list[k] = temp
            total_checks += 1
    return total_checks, input_list


print(bubble_sort(lst))
print(bubble_sort_2(lst))
