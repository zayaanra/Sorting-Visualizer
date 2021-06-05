def swap(lst, idx1, idx2):
    tmp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = tmp


def insertionSort(lst):
    i = 1
    while i < len(lst):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            swap(lst, j, j - 1)
            j -= 1
        i += 1