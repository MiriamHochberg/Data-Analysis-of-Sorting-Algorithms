
#array class to be used for building and testing different sorting algorithms 

class Array:
    
    def __init__(self, arr):
        #store copy of array 
        self.__a = arr.copy()
        
        #how many items in the array 
        self.__nItems = len(arr)
        
    # The sorting algorithms in this class are adapted from:
    # "Data Structures & Algorithms in Python" by John Canning,
    # Alan Broder, and Robert Lafore, with modifications.
        
    #bubble sort with no early exit 
    def bubbleSort(self):
        
        #work on a copy
        a = self.__a.copy()
        
        
        #outer loop starts from the end of the list (all the way to the right) 
        for last in range(self.__nItems - 1, 0, -1):
            
            #innter loop works from left to right 
            for inner in range(last):
                
                #if element to the right is smaller than the current position in
                #the list, swap them 
                if a[inner] > a[inner + 1]:
                    temp = a[inner]
                    a[inner] = a[inner + 1]
                    a[inner + 1] = temp
        
        return a
    
    
    #bubble sort with early exit
    def bubbleSortEarly(self):
        
        #work on a copy
        a = self.__a.copy()
        
        #same idea as bubble sort from above 
        for last in range(self.__nItems - 1, 0, -1):
            
            #to allow for early exit, assumes its already sorted 
            swapped = False
            
            for inner in range(last):
                
                if a[inner] > a[inner + 1]:
                    temp = a[inner]
                    a[inner] = a[inner + 1]
                    a[inner + 1] = temp
                    
                    #once there is a swap, we know it is not 100% sorted yet- stays in loop 
                    swapped = True
            
            #if no swaps that means it's already sorted so exist the loop 
            if not swapped:
                break
        
        return a
    
    
    #insertion sort
    def insertionSort(self):
        
        #work on a copy
        a = self.__a.copy()
        
        # start from index 1- second element bc 
        #  a single element (index 0) is already "sorted"        
        for outer in range(1, self.__nItems):
            
            # Store the current value we want to insert
            temp = a[outer]
            
            # Start comparing from this position
            inner = outer
            
            
             #as long as we are not at the begining and the current value is smaller than the one before it
            while inner > 0 and temp < a[inner - 1]:
                
                #move the larger element one position to the right
                a[inner] = a[inner - 1]
                
                #move one left
                inner -= 1
            
            #temp in its correct sorted position
            a[inner] = temp
        
        return a
    
    #merge sort 
    def mergeSort(self):
        
        # work on a copy of self.__a, so the original array stays unchanged
        a_copy = self.__a.copy()
        return self.splitAndRecurse(a_copy)
    
    
    #helper to merge sort. recursively splits the list and merges 
    
    def splitAndRecurse(self, arr):
        
        # Base case
        if len(arr) <= 1:
            return arr
    
        # find the middle index to split the array
        mid = len(arr) // 2
    
        # recursively sort the left half
        left = self.splitAndRecurse(arr[:mid])
    
        # recursively sort the right half
        right = self.splitAndRecurse(arr[mid:])
    
        # merge the sorted halves and return
        return self.merge(left, right)
    
    
    #helper function for merge sort bc it's called by the splitandrecurse helper fucntion 
    def merge(self, left, right):
        # hold the merged result
        ans = []  
        
        # pointers for left and right lists
        i = 0 
        j = 0      
    
        # merge elements one by one in sorted order
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1
    
        # append any remaining elements from left
        while i < len(left):
            ans.append(left[i])
            i += 1
    
        # append any remaining elements from right
        while j < len(right):
            ans.append(right[j])
            j += 1
    
        return ans

    
    #counting sort on digit- need for radix 
    def countSortOnDigit(self, arr, d):
        
        #output array 
        ans = [0] * len(arr)
        
        #list to track frequency of each digit 
        counts = [0] * 10
        
        someRemaining = False
        
        #determine digit position
        tenPower = 10 ** d
        
        
        #loop fills in the counts list- how many of each digit 0-9 there are
        for i in range(len(arr)):
            
            #gets the current digit 
            temp = arr[i] // tenPower
            
            #are there still digits?
            if temp > 0:
                someRemaining = True
                
            #counts how many times each digit appears 
            counts[temp % 10] += 1
            
        #no more digits 
        if not someRemaining:
            return False, arr
        
        #turns counts into positions. now the list contains the number of values
        #in the array whose d'th digit is <= j 
        for j in range(1, 10):
            counts[j] += counts[j - 1]
        
        #place the values of arr into correct spot in ans list 
        for i in range(len(arr) - 1, -1, -1):
            digit = (arr[i] // tenPower) % 10
            counts[digit] -= 1
            ans[counts[digit]] = arr[i]
        
        return True, ans
    
    
    #radix sort
    def radixSort(self):
        
        #work on a copy so original array stays unchanged
        a = self.__a.copy()
        
        d = 0
        
        #keep sorting by each digit until no digits left
        while True:
            
            #run counting sort on current digit
            hasMore, a = self.countSortOnDigit(a, d)
            
            #if no more digits, stop
            if not hasMore:
                break
            
            d += 1
        
        #return sorted copy
        return a
    
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 