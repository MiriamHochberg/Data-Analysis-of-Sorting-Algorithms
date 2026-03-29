from SortDemoCode import Array
import pandas as pd
import matplotlib.pyplot as plt
import random
import time

#these tests collect data to determine how effective the early 
#exit on bubble sort is compared to regular bubble sort 

#sort passes in either regular bubble or bubble with early exit 
#list type passes in either random, almost sorted, or fully sorted 
#swaps passes in in decimal form the percent that should be sorted 
#and graph if true- gets graphed right other, otherwise it's data frame gets returned 

def single_sort(sort, list_type, swaps =0, graph= True): 
    
    #if doing sorting on either random or fully sorted 
    if swaps <= 0: 
        # list of 6 different sizes for the input array
        sizes = [250, 500, 1000, 2500, 5000, 10000]    
     
    #if doing mostly sorted list- we only want one list size    
    else: 
        sizes =[5000] 
    
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
                
            #completely sorted list     
            elif list_type == "sorted": 
                arr = [j for j in range(size)] 
            
            #list mostly sorted    
            elif list_type == "almost sorted": 
                
                #create fully sorted list
                arr = [j for j in range(size)] 
                
                #making a tangible number of swaps out of the percent decimal
                #passed into the parameter
                num_swaps = int(size * swaps)
                
                #modify python shuffle method - only shuffle certain amount 
                for k in range(num_swaps): 
                    x = random.randint(0, size - 1)
                    y = random.randint(0, size - 1)
                    arr[x], arr[y] = arr[y], arr[x]
                                
            a = Array(arr)

            # start timing
            start = time.time()

            # run the correct sorting algorithm
            if sort == "Bubble":                 a.bubbleSort()
            elif sort == "Bubble with break":    a.bubbleSortEarly() 
        

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


#for when they are sorting random lists 
def bubblesRandom(): 
    noEarly = single_sort("Bubble", list_type="random", graph=False) 
    yesEarly = single_sort("Bubble with break", list_type="random", graph=False) 
   
    
    # merge into one DataFrame- axis=1, means horizontal concatination 
    combined = pd.concat([noEarly, yesEarly], axis=1)
    

    # plot comparison
    combined.plot(marker='o')
    plt.title("Bubble Sort vs Bubble Sort with Early Exit (Random Lists)")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.show()    
    
    
#for when they are sorting pre- sorted lists 
def bubblesSorted(): 
    no = single_sort("Bubble", list_type ="sorted" , graph=False) 
    yes = single_sort("Bubble with break", list_type = "sorted", graph=False) 
    
    # merge into one DataFrame- axis=1, means horizontal concatination 
    combined = pd.concat([no, yes], axis=1)
    
    # plot comparison
    combined.plot(marker='o')
    plt.title("Bubble Sort vs Bubble Sort with Early Exit (Sorted Lists)")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.show()  
    
    
#for mostly sorted list
def almost_sorted(): 
    
    #list of different percents of how shuffled the list should be 
    percents = [0.05, 0.01, 0.005, 0.0025, 0.001]
    
    #empty lists to store times of each algorithm  
    times_no = []
    times_yes = []
    
    #run the sorting for each percent sortedness 
    for p in percents: 
        no = single_sort("Bubble", list_type="almost sorted", swaps=p, graph=False)
        yes = single_sort("Bubble with break", list_type="almost sorted", swaps=p, graph=False)
        
        # each DataFrame has only one row bc size 5000 , get that value and add to new list 
        times_no.append(no.iloc[0,0])
        times_yes.append(yes.iloc[0,0])
    
    # create a single DataFrame for plotting
    df = pd.DataFrame({
        "Bubble": times_no,
        "Bubble with Early Exit": times_yes
    }, index=percents)
    

    # plot
    df.plot(marker='o')
    plt.title("Bubble Sort vs Bubble Sort with Early Exit (Mostly Sorted List)")
    plt.xlabel("Percent of List Swapped")
    plt.ylabel("Time (seconds)")
    #make larger percents on left 
    plt.gca().invert_xaxis() 
    plt.grid()
    plt.show()
        
        
def main():
    print("These graphs compare the performance of regular bubble sort vs. bubble sort with the option to break early") 
    print("To see graph for random list- select 1") 
    print("To see graph for fully sorted list- select 2") 
    print("To see graph for mostly sorted list- select 3") 
    
    choice = input("Enter your choice (1/2/3): ")
        
    if choice == "1":
        bubblesRandom()
    elif choice == "2":
        bubblesSorted()
    elif choice == "3":
        almost_sorted()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    
    
main()
        
        
