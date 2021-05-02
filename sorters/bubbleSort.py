def swap(lst, idx1, idx2):
    tmp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = tmp


def bubbleSort(lst):
    n = len(lst)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                swap(lst, j + 1, j)



