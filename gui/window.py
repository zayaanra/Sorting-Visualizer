from tkinter import *

# Initialize root
root = Tk()
root.title("Sorting Visualizer")
root.maxsize(2000, 1000)
root.config(bg="white")

selected = StringVar()

# Create a toolbar at the top
bar = Frame(root, bg='black')

# List of various sorting algorithms
options = ["Bubble Sort", "Merge Sort", "Quick Sort"]
selected.set(options[0])

# Create dropdown menu for algorithm selection
dropdown = OptionMenu(bar, selected, *options)
dropdown.pack(side=LEFT, padx=3, pady=3)

bar.pack(side=TOP, fill=X)

root.mainloop()
