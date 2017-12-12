def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    lesser = [item for item in arr[1:] if item <= pivot]
    greater = [item for item in arr[1:] if item > pivot]
    return quicksort(lesser) + [pivot] + quicksort(greater)