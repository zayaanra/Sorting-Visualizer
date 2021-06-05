# Swap elements in array
def swap(data, idx1, idx2):
    tmp = data[idx1]
    data[idx1] = data[idx2]
    data[idx2] = tmp


# Sort in place
def partition(data, low, high):
    pivot = data[high]
    mid = low - 1
    for i in range(low, high):
        if data[i] < pivot:
            mid += 1
            swap(data, mid, i)
    swap(data, mid + 1, high)
    return mid + 1


# Quick Sort Algorithm
def quickSort(data, low, high):
    if len(data) == 1:
        return data
    if low < high:
        p = partition(data, low, high)
        quickSort(data, low, p - 1)
        quickSort(data, p + 1, high)
