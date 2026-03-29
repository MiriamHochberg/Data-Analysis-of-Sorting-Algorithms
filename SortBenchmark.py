from SortDemoCode import Array
import pandas as pd
import matplotlib.pyplot as plt
import random
import time


#function to run, find times, collect data, and graph perfomance of each 
#sorting algorithm on its own 

#function takes in what sorting algorithm to run, the appropiate list 
#size for that algorithm, the type of list, and whether the results should be graphed 
def single_sort(sort, array_size, list_type="random", graph=True):
    
    # list of 6 different sizes for the input array- for bubble and insertion
    small_sizes = [250, 500, 1000, 2500, 5000, 10000]
    
    # list of 6 different sizes for the input array- for merge and radix
    big_sizes =[250, 1000, 5000, 25000, 50000, 100000]
    
    #assigning the sorting algorithm the appropiate list 
    sizes = small_sizes if array_size == "small" else big_sizes
    
    # empty list to collect average times
    times = []

    #for each size in the list of sizes 
    for size in sizes:
        
        #variable to collect total time it took to run for that size list 
        total_time = 0

        # run multiple trials for more accurate results 
        for i in range(5):  
            
            #give list the appropiate content 
            
            if list_type == "random": 
                # create random array
                arr = [random.randint(0, 5000) for j in range(size)]
             
             #only used for radix vs merge 
            elif list_type== "big random": 
                arr = [random.randint(10**14, 10**15 - 1) for j in range(size)]
                
            #completely sorted list     
            elif list_type == "sorted": 
                arr = [j for j in range(size)] 
                
            elif list_type == "reverse": 
                arr= [j for j in range(size-1, -1, -1)] 
            
            #list mostly sorted    
            elif list_type == "almost sorted": 
                
                #create fully sorted list
                arr = [j for j in range(size)] 
                
                #modify python shuffle method - only 5 out of place 
                for k in range(5): 
                    x = random.randint(0, size - 1)
                    y = random.randint(0, size - 1)
                    arr[x], arr[y] = arr[y], arr[x]
                                
            a = Array(arr)

            # start timing
            start = time.time()

            # run the correct sorting algorithm
            if sort == "Bubble":                 a.bubbleSort() 
            elif sort == "Bubble Early":         a.bubbleSortEarly()
            elif sort == "Insertion":            a.insertionSort()
            elif sort == "Merge":                a.mergeSort()
            elif sort == "Radix":                a.radixSort()

            # end timing
            end = time.time()
            
            #add that time to the total time for the current list size 
            total_time += (end - start)

        # average time over 5 trials
        average = total_time / 5
        times.append(average)

    #build dictionary where the keys are the sorting type and the average times 
    #for each input size 
    Sortdata = {sort + " Sort": times}

    # DataFrame with data collected 
    df = pd.DataFrame(Sortdata, index=sizes)
    
    #only graph if passed in True to the parameter 
    if graph: 
        #plotting graph of the df 
        df.plot(marker='o')
        plt.title(sort + " Sort Performance")
        plt.xlabel("Input Size")
        plt.ylabel("Time (seconds)")
        plt.grid()
        plt.show()

    return df



#these tests are useed to compare bubble vs insertion 

#bubble compared to insertion - random 
def bubble_insertion_random(): 
    bubble = single_sort("Bubble", "small", list_type = "random", graph=False) 
    insertion = single_sort("Insertion", "small", list_type = "random", graph=False) 
    
    combined = pd.concat([bubble, insertion], axis = 1) 
    

    # plot comparison
    combined.plot(marker='o')
    plt.title("Insertion Sort vs Bubble Sort (Random Lists)")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.show()         
    
    


#bubble compared to insertion- sorted
def bubble_insertion_sorted(): 
    bubble = single_sort("Bubble", "small", list_type = "sorted", graph=False) 
    insertion = single_sort("Insertion", "small", list_type = "sorted", graph=False) 
    bubbleEarly = single_sort("Bubble Early", "small", list_type="sorted", graph= False)
    
    combined = pd.concat([bubble, insertion, bubbleEarly], axis = 1) 
   
    
    # plot comparison
    combined.plot(marker='o')
    plt.title("Insertion Sort vs Bubble  (Sorted Lists)")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.show()    
        


#bubble  compared to insertion- almost sorted 
def bubble_insertion_almostSorted(): 
    bubble = single_sort("Bubble", "small", list_type = "almost sorted", graph=False) 
    insertion = single_sort("Insertion", "small", list_type = "almost sorted", graph=False) 
    bubbleEarly = single_sort("Bubble Early", "small", list_type="almost sorted", graph= False)
    
    
    combined = pd.concat([bubble, insertion, bubbleEarly], axis = 1) 
    
    # plot comparison
    combined.plot(marker='o')
    plt.title("Insertion Sort vs Bubble Sort (Mostly Sorted Lists)")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.show()  
    
def bubble_insertion_reverse(): 
    bubble = single_sort("Bubble", "small", list_type = "reverse", graph=False) 
    insertion = single_sort("Insertion", "small", list_type = "reverse", graph=False) 
    
    combined = pd.concat([bubble, insertion], axis = 1) 
    
    # plot comparison
    combined.plot(marker='o')
    plt.title("Insertion Sort vs Bubble Sort (Reverse Lists)")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.show()      
    


#these tests are used to compare merge vs radix 

#merge vs radix - random 
def merge_radix_random(): 
    
    merge = single_sort("Merge", "big", list_type= "random", graph= False) 
    
    radix = single_sort("Radix", "big", list_type= "random", graph= False) 
    
    combined= pd.concat([merge, radix], axis=1) 
    
    # plot comparison
    combined.plot(marker='o')
    plt.title("Merge Sort vs Radix (Random Lists)")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.show()    

#merge vs radix- sorted 
def merge_radix_sorted(): 
    
    merge = single_sort("Merge", "big", list_type= "sorted", graph= False) 
    
    radix = single_sort("Radix", "big", list_type= "sorted", graph= False) 
    
    combined= pd.concat([merge, radix], axis=1) 
    
    # plot comparison
    combined.plot(marker='o')
    plt.title("Merge Sort vs Radix (Sorted Lists)")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.show()        
    

#merge vs radix- almost sorted 
def merge_radix_almost_sorted(): 
    
    merge = single_sort("Merge", "big", list_type= "almost sorted", graph= False) 
    
    radix = single_sort("Radix", "big", list_type= "almost sorted", graph= False) 
    
    combined= pd.concat([merge, radix], axis=1) 
    
    # plot comparison
    combined.plot(marker='o')
    plt.title("Merge Sort vs Radix (Mostly Sorted Lists)")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.show() 
    
    
#merge vs radix- reverse
def merge_radix_reverse(): 
    
    merge = single_sort("Merge", "big", list_type= "reverse", graph= False) 
    
    radix = single_sort("Radix", "big", list_type= "reverse", graph= False) 
    
    combined= pd.concat([merge, radix], axis=1) 
    
    # plot comparison
    combined.plot(marker='o')
    plt.title("Merge Sort vs Radix (Reversed Lists)")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.show() 


#merge vs radix- huge random lists (so that radix is slower than merge) 
def merge_radix_big(): 
    
    merge = single_sort("Merge", "big", list_type= "big random", graph= False) 
    
    radix = single_sort("Radix", "big", list_type= "big random", graph= False) 
    
    combined= pd.concat([merge, radix], axis=1) 

    # plot comparison
    combined.plot(marker='o')
    plt.title("Merge Sort vs Radix (Big Random)")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.show() 


#interactive main function to try out all the tests 
def main():
    print("Welcome to the Sorting Test Program!")
    
    # Ask which group of tests (insertion vs bubble or merge vs radix) 
    group_choice = input(
        "Choose test group:\n"
        "1 - Insertion Sort vs Bubble Sort\n"
        "2 - Merge Sort vs Radix Sort\n"
        "Enter 1 or 2: "
    )
    
    if group_choice == "1":
        # Bubble vs Insertion tests
        print("\nYou chose Insertion vs Bubble tests.")
        print("Choose specific test type:")
        print("1 - Random lists")
        print("2 - Sorted lists")
        print("3 - Mostly sorted lists")
        print("4 - Reverse lists")
        
        test_choice = input("Enter 1, 2, 3, or 4: ")
        
        if test_choice == "1":
            bubble_insertion_random()
        elif test_choice == "2":
            bubble_insertion_sorted()
        elif test_choice == "3":
            bubble_insertion_almostSorted()
        elif test_choice == "4":
            bubble_insertion_reverse()
        else:
            print("Invalid choice.")
    
    elif group_choice == "2":
        # Merge vs Radix tests
        print("\nYou chose Merge vs Radix tests.")
        print("Choose specific test type:")
        print("1 - Random lists")
        print("2 - Sorted lists")
        print("3 - Mostly sorted lists")
        print("4 - Reverse lists")
        print("5 - Very large random numbers (big random)")
        
        test_choice = input("Enter 1, 2, 3, 4, or 5: ")
        
        if test_choice == "1":
            merge_radix_random()
        elif test_choice == "2":
            merge_radix_sorted()
        elif test_choice == "3":
            merge_radix_almost_sorted()
        elif test_choice == "4":
            merge_radix_reverse()
        elif test_choice == "5":
            merge_radix_big()
        else:
            print("Invalid choice.")
    
    else:
        print("Invalid group choice.")
    
    
    
 
if __name__ == "__main__":
    main()







  
