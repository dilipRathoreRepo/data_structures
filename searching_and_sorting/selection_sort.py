lst = [9, 4, 5, 3, 1, 2]


def selection_sort(arr):
    for fillslots in range(len(arr)-1, 0, -1):
        maxPosition = 0
        for location in range(1, fillslots+1):
            if arr[location] > arr[maxPosition]:
                maxPosition = location
        tmp = arr[fillslots]
        arr[fillslots] = arr[maxPosition]
        arr[maxPosition] = tmp
    return arr


print(selection_sort(lst))
