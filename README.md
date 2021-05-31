# Sorting-Visualizer

A sorting visualizer that implements various sorting algorithms and visualizes onto a Python GUI using tkinter.

# Algorithms
This project implements different sorting algorithms. The current algorithms implemented include:

## Bubble sort
Bubble sort is a sorting algorithm that is often used a learning tool. In most cases, bubble sort is an inefficient algorithm with a worst-case runtime of O(n^2). In some cases, it may end up in a O(n) scenario. It involves looping through a data set twice and comparing elements with each other in order to "swap" and sort them.

## Merge sort
Merge sort is a sorting algorithm based on the divide-and-conquer technique. The process involves splitting an array of elements up until you can get to it's smallest possible split - which at that point, you will merge based on comparison of each element with each other. Runs in O(nlogn) in worst and best case scenarios.

## Quick sort
Quick sort is a sorting algorithm that also utilizes the divide-and-conquer technique. Instead of directly splitting up the array, quick sort uses a technique known as partitioning. This involves moving through the array and swapping elements based on a location in the array called the "pivot". After the swapping is completed, recursive calls are made to sort the data set. Worst-case runtime is O(n^2) when all elements or either smaller or larger than the pivot. It has an average runtime of O(nlogn). 

# GUI
The GUI consists of a dropdown menu to select the desired algorithm, a color to represent the data set, an input size determined by the user as well as a START/PAUSE/GENERATE button that starts the sorting, pauses it, and generates a data set respectively.

## Before the Sort
![test](https://prnt.sc/13nf7ng)




## After the Sort
