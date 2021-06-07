# Sort in place
def partition(data, low, high):
    pivot = data[high]
    mid = low - 1
    for i in range(low, high):
        if data[i] < pivot:
            mid += 1
            data[mid], data[i] = data[i], data[mid]
    data[mid+1], data[high] = data[high], data[mid+1]
    return mid + 1


# Quick Sort Algorithm
def quickSort(data, low, high):
    if len(data) == 1:
        return data
    if low < high:
        p = partition(data, low, high)
        quickSort(data, low, p - 1)
        quickSort(data, p + 1, high)
