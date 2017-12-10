def array_sum(arr):
    if arr == []:
        return 0
    return arr[0] + array_sum(arr[1:])

def count_items(arr):
    if arr == []:
        return 0
    return 1 + count_items(arr[1:])

def find_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max