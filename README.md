# Data-Analysis-of-Sorting-Algorithms

## Overview 
### This project explores how different sorting algorithms in Python perform on arrays of varying sizes. I ran experiments and collected the data with Pandas, then used Matplotlib to visualize performance trends. Working on this project gave me practical experience working with data and understanding how algorithms behave in practice.

## Graph Comparing the 4 tested algorithms 

## Bubble Sort with Early Exit vs. Bubble Sort without early exit 
### When it comes to Bubble Sort, it can be run with the ability to exit early if no swaps happened. I wanted to see how effective it is to run that code when compared to running bubble sort without that abiblity. 
### First, here is a graph that shows how each performs when sorting random lists of different sizes. 

### <img width="631" height="473" alt="bubblesRandom" src="https://github.com/user-attachments/assets/f327aaa4-808c-4215-8f4d-366d29f8ea48" />

### Here we see that the time it takes the bubble sort with the early exit even a little longer than it takes the regular bubble sort. this is because... 

### now let's look at how each performs on a fully sorted list 
# <img width="620" height="463" alt="bubblesSorted" src="https://github.com/user-attachments/assets/a3cbeec5-47ce-4ded-b98d-b0688f7e1957" />

### Here we see that the one with early exist works much faster and stays constant at a fraction of a second 

### Based on this my question is at what point of a list being sorted does the early exit feauture become impacful? And below is a graph showing the results of how each performed when dealing with a list of only 5,000 numbers- and the independent variable is the percent of the list that is out of order. 

# <img width="629" height="478" alt="bubbleAlmostFinal" src="https://github.com/user-attachments/assets/f965eebc-863f-4efb-93dd-4583f3aa0427" />

### From here we see that at the point where the line for early exit drops below the regular bubble sort is at the turning point is at 1% and below that's where see the early exit having the biggest impact on the time it takes to sort. 




## Bubble Sort vs. Insertion 

## Testing Merge sort vs. Radix Sort 

