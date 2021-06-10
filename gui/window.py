import random
from time import sleep
import sorters.bubbleSort
from sorters.mergeSort import mergeSort
from sorters.quickSort import quickSort
from sorters.insertionSort import insertionSort
from tkinter import *

# Event-Handlers
num_to_bar = []
random_data = []


# TODO - Fix imports for sorters and animate()


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
        sorters.bubbleSort.bubbleSort(num_to_bar)
    elif algo == "Merge Sort":
        sorted_data = mergeSort(random_data)
    elif algo == "Quick Sort":
        quickSort(random_data, 0, len(random_data) - 1)
    elif algo == "Insertion Sort":
        insertionSort(random_data)


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
