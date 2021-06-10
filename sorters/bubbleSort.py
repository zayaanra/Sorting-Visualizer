import gui.window


# lst - data to sort
# bars - used to animate the sort
def bubbleSort(lst):
    n = len(lst)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
                gui.window.animate(lst[j][1], lst[j + 1][1])
