import random
from sorters.bubbleSort import bubbleSort
from tkinter import *

# Event-Handlers
bars = []
random_data = []
sorted_data = []


# TODO - Possibly refactor things around to make code cleaner
# Draws data set out every time the "Generate" button is pressed
def draw_new():
    # Generate random data dependent on the user input size
    bars.clear()
    random_data.clear()
    length = slider.get()
    [random_data.append(random.randint(-125, 125)) for _ in range(1, length + 1)]
    user_choice = color.get()
    # Delete the current dataset
    canvas.delete("all")
    # Offsets used to determine the distance away from each bar
    x1_offset = 10
    x2_offset = 20
    # Loop through randomly generated dataset and draw each number out as a bar
    for i in random_data:
        c = canvas.create_rectangle(x1_offset, 0, x2_offset, (abs(i) + (i / 100) * 3) + 50, fill=str(user_choice))
        bars.append(c)
        x1_offset += 10
        x2_offset += 10
    canvas.pack(side=BOTTOM)


# TODO - Negative numbers break when being represented in the GUI - fix calculation?
def draw_sorted(data):
    user_choice = color.get()
    canvas.delete("all")
    x1_offset = 10
    x2_offset = 20
    for i in data:
        canvas.create_rectangle(x1_offset, 0, x2_offset, (abs(i) + (i / 100) * 3) + 50, fill=str(user_choice))
        x1_offset += 10
        x2_offset += 10
    canvas.pack(side=BOTTOM)


def start_sort():
    # Selected Sorting Algorithm
    # algo = selected.get()
    bubbleSort(random_data)
    draw_sorted(random_data)


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
options = ["Bubble Sort", "Merge Sort", "Quick Sort"]
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

# Create a button to pause the visualization
pause = Button(bar, text="Pause")
pause.pack(side=LEFT, padx=3, pady=3)

# Create a canvas
canvas = Canvas(width=2000, height=930, bg="grey")

# Create a button to generate a random data set
generate = Button(bar, text="Generate", command=draw_new)
generate.pack(side=LEFT, padx=3, pady=3)

bar.pack(side=TOP, fill=X)

root.mainloop()
