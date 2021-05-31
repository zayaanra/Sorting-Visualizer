import random
from tkinter import *


# Event-Handlers

# Draws data set out every time the "Generate" button is pressed
def draw():
    # Generate random data dependent on the user input size
    length = slider.get()
    data = [random.randint(-100, 100) for _ in range(1, length+1)]
    user_choice = color.get()
    # Delete the current dataset
    canvas.delete("all")
    # Offsets used to determine the distance away from each bar
    x1_offset = 50
    x2_offset = 75
    # Loop through randomly generated dataset and draw each number out as a bar
    for i in data:
        # TODO - Need to figure out to correctly place each rectangle next to each other, no padding should exist
        # TODO - Height of each rectangle should change depending on the number it represents
        # TODO - Make rectangles thinner to fit in more?
        canvas.create_rectangle(x1_offset, 0, x2_offset, 500, fill=str(user_choice))
        canvas.create_text((x1_offset+10, 75), text=str(i), font=("freemono", 11, "bold"))
        x1_offset += 50
        x2_offset += 50
    canvas.pack(side=BOTTOM)


# Initialize root
root = Tk()
root.title("Sorting Visualizer")
# Set maximum window size
root.maxsize(1500, 1000)

# Set window size when application is first opened
root.geometry("1500x1000")

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
slider = Scale(bar, label="Input Size", from_=1, to=100, length=400, resolution=1, orient=HORIZONTAL)
slider.pack(side=LEFT, padx=3, pady=3)

# Create a second dropdown menu to allow user to customize color of visualization
customizable = OptionMenu(bar, color, *colors)
customizable.pack(side=LEFT, padx=3, pady=3)

# Create a button to start the visualization
start = Button(bar, text="Start")
start.pack(side=LEFT, padx=3, pady=3)

# Create a button to pause the visualization
pause = Button(bar, text="Pause")
pause.pack(side=LEFT, padx=3, pady=3)

# Create a canvas
canvas = Canvas(width=2000, height=930, bg="grey")

# Create a button to generate a random data set
generate = Button(bar, text="Generate", command=draw)
generate.pack(side=LEFT, padx=3, pady=3)

bar.pack(side=TOP, fill=X)

root.mainloop()
