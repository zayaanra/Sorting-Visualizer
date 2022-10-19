import random
from time import sleep
from tkinter import *

########################## SORTERS ##########################
def bubbleSort(lst):
    n = len(lst)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
                animate(lst[j][1], lst[j + 1][1])

def insertionSort(lst):
    i = 1
    while i < len(lst):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            animate(lst[j][1], lst[j - 1][1])
            j -= 1
        i += 1

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

# Sort in place
def partition(data, low, high):
    pivot = data[high]
    mid = low - 1
    for i in range(low, high):
        if data[i] < pivot:
            mid += 1
            data[mid], data[i] = data[i], data[mid]
            animate(data[i][1], data[mid][1])
    data[mid+1], data[high] = data[high], data[mid+1]
    animate(data[high][1], data[mid+1][1])
    return mid + 1


# Quick Sort Algorithm
def quickSort(data, low, high):
    if len(data) == 1:
        return data
    if low < high:
        p = partition(data, low, high)
        quickSort(data, low, p - 1)
        quickSort(data, p + 1, high)

#############################################################



# Event-Handlers
num_to_bar = []
random_data = []


# Draws data set out every time the "Generate" button is pressed
def generate():
    # Delete the current dataset
    num_to_bar.clear()
    random_data.clear()
    # Retrieve user inputs
    length = slider.get()
    user_choice = str(color.get())
    canvas.delete("all")
    # Generate random data dependent on the user input size
    [random_data.append(random.randint(1, 500)) for _ in range(1, length + 1)]
    # Offsets used to determine x-coord of bar
    x1_offset = 10
    x2_offset = 20
    # Loop through randomly generated dataset and draw each number out as a bar
    for num in random_data:
        bar = canvas.create_rectangle(x1_offset, 0, x2_offset, (num + (num / 100) * 3) + 50, fill=user_choice)
        num_to_bar.append((num, bar))
        x1_offset += 10
        x2_offset += 10
    canvas.pack(side=BOTTOM)


def animate(item, item2):
    user_choice = str(color.get())
    canvas.itemconfig(item, fill="white")
    sleep(0.04)
    root.update_idletasks()
    x0, _, x1, _ = canvas.coords(item)
    x2, _, x3, _ = canvas.coords(item2)
    canvas.move(item, x2 - x0, 0)
    canvas.move(item2, x1 - x3, 0)
    canvas.itemconfig(item, fill=user_choice)


def start_sort():
    # Selected Sorting Algorithm
    algo = str(selected.get())
    if algo == "Bubble Sort":
        bubbleSort(num_to_bar)
    elif algo == "Merge Sort":
        # TODO - need to fix
        mergeSort(num_to_bar)
    elif algo == "Quick Sort":
        quickSort(num_to_bar, 0, len(num_to_bar) - 1)
    elif algo == "Insertion Sort":
        insertionSort(num_to_bar)


# Initialize root
root = Tk()
root.title("Sorting Visualizer")
# Set maximum window size
root.maxsize(1265, 800)

# Set window size when application is first opened
root.geometry("1265x800")

root.config(bg="white")

# Used for dropdown menus
selected = StringVar()
color = StringVar()

# Create a toolbar at the top
toolbar = Frame(root, bg='black')

# Set variables and other data
options = ["Bubble Sort", "Merge Sort", "Quick Sort", "Insertion Sort"]
selected.set(options[0])
colors = ["Blue", "Red", "Yellow", "Green", "Orange", "Pink", "Purple"]
color.set(colors[0])

# Create label and dropdown menu for algorithm selection
dropdown = OptionMenu(toolbar, selected, *options)
dropdown.pack(side=LEFT, padx=3, pady=3)

# Create a slider to determine input size
slider = Scale(toolbar, label="Input Size", from_=1, to=125, length=400, resolution=1, orient=HORIZONTAL)
slider.pack(side=LEFT, padx=3, pady=3)

# Create a second dropdown menu to allow user to customize color of visualization
customizable = OptionMenu(toolbar, color, *colors)
customizable.pack(side=LEFT, padx=3, pady=3)

# Create a button to start the visualization
start = Button(toolbar, text="Start", command=start_sort)
start.pack(side=LEFT, padx=3, pady=3)

# Create a canvas
canvas = Canvas(width=2000, height=930, bg="grey")

# Create a button to generate a random data set
generator = Button(toolbar, text="Generate", command=generate)
generator.pack(side=LEFT, padx=3, pady=3)

toolbar.pack(side=TOP, fill=X)

root.mainloop()
