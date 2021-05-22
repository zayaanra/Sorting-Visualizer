from tkinter import *

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
slider = Scale(bar, label="Input Size", from_=0, to=100, length=400, resolution=1, orient=HORIZONTAL)
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

bar.pack(side=TOP, fill=X)

root.mainloop()
