# Data-Analysis-of-Sorting-Algorithms

## Overview 
### This project analyzes the performance of four sorting algorithms in Python across different input sizes and conditions. I used Pandas to collect timing data and Matplotlib to visualize it, I explored three questions:
#### How much does the early exit optimization improve Bubble Sort?
#### How does Insertion Sort compare to Bubble Sort despite sharing the same O(n²) complexity?
#### When is Radix Sort faster than Merge Sort, and when is Merge Sort the better choice?

## Bubble Sort vs. Bubble Sort with Early Exit
#### For Bubble Sort, there’s an option to exit early if no swaps happen during a pass. I wanted to see how much of a difference this feature makes compared to the regular Bubble Sort.

## Random Lists 
#### Here’s a graph showing how each performs when sorting random lists of different sizes:

# <img width="631" height="473" alt="bubblesRandom" src="https://github.com/user-attachments/assets/f327aaa4-808c-4215-8f4d-366d29f8ea48" />

#### We can see that the Bubble Sort with early exit actually takes a little longer than the regular Bubble Sort on random lists. This is because the check for no swaps adds a tiny bit of overhead, which doesn’t pay off when the list is mostly unsorted.

## Fully Sorted Lists
#### Now let’s see how each algorithm performs on a fully sorted list:
# <img width="620" height="463" alt="bubblesSorted" src="https://github.com/user-attachments/assets/a3cbeec5-47ce-4ded-b98d-b0688f7e1957" />

#### Here we can see a clear benefit- the Bubble Sort with early exit finishes much faster because it detects that no swaps are needed and stops immediately. This is Bubble Sort at its best case performance- O(n) 

## Mostly Sorted Lists

### This made me curious- at what point does the early exit feature start making a noticeable impact? To test this, I ran both algorithms on a list of 5,000 numbers where a certain percentage of the list was out of order.


# <img width="629" height="478" alt="bubbleAlmostFinal" src="https://github.com/user-attachments/assets/f965eebc-863f-4efb-93dd-4583f3aa0427" />

#### From this graph, we can see that the two algorithms perform similarly until the list is about 0.5% out of order. Below this point, the early exit begins to pull ahead, and the benefit grows dramatically as the list approaches fully sorted. 

## Testing Bubble Sort vs. Insertion Sort 

#### Bubble Sort and Insertion Sort are both O(n^2)- meaning that as the input list grows, the amount of work scales at a quadratic rate. However, this does not mean that Bubble Sort and Insertion sort have the same performance times because differences in how they process data can lead to significantly different runtimes. For example, the graph below demonstrates graphically how they are O(n^2), but insertion sort is faster.
# <img width="632" height="480" alt="B_i_random" src="https://github.com/user-attachments/assets/0a9426e0-9308-4974-b7b8-1049d06b6eb3" />
#### This difference occurs because of how each algorithm handles elements. Bubble Sort repeatedly compares and swaps adjacent elements, even if they are already close to their correct position. This leads to many unnecessary comparisons and swaps. In contrast, Insertion Sort places each element directly into its correct position by shifting larger elements to the right. This reduces the number of operations needed, especially when elements are already somewhat ordered. As a result, even though both algorithms have the same O(n^2) time complexity, Insertion Sort is generally more efficient in practice and performs significantly better on most inputs.

## Testing Merge sort vs. Radix Sort 
#### Merge Sort runs in O(n log n), while Radix Sort runs in O(nk), where k is the number of digits in the largest number. For typical inputs, k is small and Radix Sort is faster, as shown in the graph below. 
# <img width="632" height="471" alt="r-m-random" src="https://github.com/user-attachments/assets/42bcaa3b-3ac1-4cec-9b4d-de5c383c91e3" />
#### However, when sorting very large numbers, in this case 15-digit numbers, Radix Sort must make 15 passes through the array, one for each digit. At this point the extra passes outweigh its usual advantage, and Merge Sort becomes the faster option.

# <img width="624" height="478" alt="r-m-huge" src="https://github.com/user-attachments/assets/016245b9-20a3-410f-92c6-5bb2124d21b2" />
#### Also, Merge Sort also has another advantage: Radix Sort can only handle non-negative integers, while Merge Sort works on any comparable data type including negatives, decimals, and strings.

## Key Takeaways 
#### Early exit significantly improves Bubble Sort on nearly sorted data but adds slight overhead on random data.
#### Insertion Sort consistently outperforms Bubble Sort despite both being O(n²).
#### Radix Sort is faster for typical inputs as compared to Merge Sort, but its performance decreases as the number of digits increases.


## Files 
#### SortDemoCode.py contains the array class and the different sorting algorithms. 
#### sortBubbleTest.py contains the function and tests for Bubble Sort with early exit vs. regular Bubble Sort 
#### SortBenchmark.py contains the function and tests for Insertion Sort vs. Bubble Sort and Merge Sort vs. Radix Sort 
#### All Sorts Graphs contains more graphs relating to the different sorting algorithms 



