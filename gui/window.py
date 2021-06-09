import random
from time import sleep
from sorters.bubbleSort import bubbleSort
from sorters.mergeSort import mergeSort
from sorters.quickSort import quickSort
from sorters.insertionSort import insertionSort
from tkinter import *

# Event-Handlers
bars = []
random_data = []


# TODO - Possibly refactor things around to make code cleaner
# Draws data set out every time the "Generate" button is pressed
def generate():
    # Delete the current dataset
    bars.clear()
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
    for i in random_data:
        c = canvas.create_rectangle(x1_offset, 0, x2_offset, (i + (i / 100) * 3) + 50, fill=user_choice)
        bars.append(c)
        x1_offset += 10
        x2_offset += 10
    canvas.pack(side=BOTTOM)


def animate(data, i):
    user_choice = str(color.get())
    # canvas.delete("all")
    x1_offset = 10
    x2_offset = 20
    delay = 0
    # for i in data:
    # canvas.create_rectangle(x1_offset, 0, x2_offset, (i + (i / 100) * 3) + 50, fill=str(user_choice))
    # x1_offset += 10
    # x2_offset += 10
    for i in bars:
        # Change current bar to white
        canvas.itemconfig(i, fill="white")
        # Sleep for 0.2 ms
        sleep(0.2)
        root.update_idletasks()
        # Change back to org. color
        canvas.itemconfig(i, fill=user_choice)
    canvas.pack(side=BOTTOM)


def start_sort():
    # Selected Sorting Algorithm
    algo = str(selected.get())
    if algo == "Bubble Sort":
        bubbleSort(random_data)
        animate(random_data, 0)
    elif algo == "Merge Sort":
        sorted_data = mergeSort(random_data)
        animate(sorted_data, 0)
    elif algo == "Quick Sort":
        quickSort(random_data, 0, len(random_data) - 1)
        animate(random_data, 0)
    elif algo == "Insertion Sort":
        insertionSort(random_data)
        animate(random_data, 0)


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
bar = Frame(root, bg='black')

# Set variables and other data
options = ["Bubble Sort", "Merge Sort", "Quick Sort", "Insertion Sort"]
selected.set(options[0])
colors = ["Blue", "Red", "Yellow", "Green", "Orange", "Pink", "Purple"]
color.set(colors[0])

# Create label and dropdown menu for algorithm selection
dropdown = OptionMenu(bar, selected, *options)
dropdown.pack(side=LEFT, padx=3, pady=3)

# Create a slider to determine input size
slider = Scale(bar, label="Input Size", from_=1, to=125, length=400, resolution=1, orient=HORIZONTAL)
slider.pack(side=LEFT, padx=3, pady=3)

# Create a second dropdown menu to allow user to customize color of visualization
customizable = OptionMenu(bar, color, *colors)
customizable.pack(side=LEFT, padx=3, pady=3)

# Create a button to start the visualization
start = Button(bar, text="Start", command=start_sort)
start.pack(side=LEFT, padx=3, pady=3)

# Create a canvas
canvas = Canvas(width=2000, height=930, bg="grey")

# Create a button to generate a random data set
generator = Button(bar, text="Generate", command=generate)
generator.pack(side=LEFT, padx=3, pady=3)

bar.pack(side=TOP, fill=X)

root.mainloop()
