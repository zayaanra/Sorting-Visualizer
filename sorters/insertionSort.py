def insertionSort(lst):
    i = 1
    while i < len(lst):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
        i += 1
