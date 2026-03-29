# Data-Analysis-of-Sorting-Algorithms

## Overview 
### This project explores how different sorting algorithms in Python perform on arrays of varying sizes. I ran experiments and collected the data with Pandas, then used Matplotlib to visualize performance trends. Working on this project gave me practical experience working with data and understanding how algorithms behave in practice.

## Graph Comparing the 4 tested algorithms 

## Bubble Sort vs. Bubble Sort with Early Exit

## Random Lists 

### For Bubble Sort, there’s an option to exit early if no swaps happen during a pass. I wanted to see how much of a difference this feature makes compared to the regular Bubble Sort.
### Here’s a graph showing how each performs when sorting random lists of different sizes:

# <img width="631" height="473" alt="bubblesRandom" src="https://github.com/user-attachments/assets/f327aaa4-808c-4215-8f4d-366d29f8ea48" />

### We can see that the Bubble Sort with early exit actually takes a little longer than the regular Bubble Sort on random lists. This is because the check for no swaps adds a tiny bit of overhead, which doesn’t pay off when the list is mostly unsorted.

## Fully Sorted Lists
### Now let’s see how each algorithm performs on a fully sorted list:
# <img width="620" height="463" alt="bubblesSorted" src="https://github.com/user-attachments/assets/a3cbeec5-47ce-4ded-b98d-b0688f7e1957" />

### Here we can see a clear benefit- the Bubble Sort with early exit finishes much faster and stays nearly constant, because it detects that no swaps are needed and stops immediately.

## Mostly Sorted Lists

### This made me curious- at what point does the early exit feature start making a noticeable impact? To test this, I ran both algorithms on a list of 5,000 numbers where a certain percentage of the list was out of order.


# <img width="629" height="478" alt="bubbleAlmostFinal" src="https://github.com/user-attachments/assets/f965eebc-863f-4efb-93dd-4583f3aa0427" />

### From this graph, we can see that the early exit feature starts to significantly reduce sorting time when about 1% of the list is out of order. Below this point, the impact is even more noticeable- the more sorted the list is, the faster the early exit makes Bubble Sort.




## Bubble Sort vs. Insertion 

## Testing Merge sort vs. Radix Sort 

