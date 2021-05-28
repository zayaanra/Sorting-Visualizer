from tkinter import *


def draw(data, color):
    # Create a canvas
    canvas = Canvas(width=2000, height=930, bg="grey")
    # Offsets used to determine the distance away from each bar
    x1_offset = 50
    x2_offset = 75
    # Loop through randomly generated dataset and draw each number out as a bar
    for i in data:
        # TODO - Need to figure out to correctly place each rectangle next to each other, no padding should exist
        # TODO - Height of each rectangle should change depending on the number it represents
        canvas.create_rectangle(x1_offset, 0, x2_offset, 500, fill="red")
        x1_offset += 50
        x2_offset += 50
    return canvas
