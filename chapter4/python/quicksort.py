def quicksort(arr):
    if len(arr) < 1:
        return arr
    pivot = arr[0]
    lesser = [item for item in arr if item <= arr[1:]]
    greater = [item for item in arr if item > arr[1:]]
    return quicksort(lesser) + [pivot] + quicksort(greater)