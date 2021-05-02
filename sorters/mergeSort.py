def merge(left, right):
    # i = index for left half, j = index for right half
    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Merge the left and right
    merged = merged + left[i:] + right[j:]
    return merged


def mergeSort(array):
    # Base case
    if len(array) <= 1:
        return array
    else:
        # Recursive case
        middle = len(array) // 2
        (left, right) = (mergeSort(array[:middle]), mergeSort(array[middle:]))
        return merge(left, right)

