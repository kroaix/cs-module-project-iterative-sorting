def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        #go to the middle
        middle = (low + high) // 2
        #is middle less than the target
        #if less, eliminate right hand side
        if target < arr[middle]:
            #high is now the middle
            high = middle - 1
        #is middle more than the target
        #if more, eliminate left side
        elif target > arr[middle]:
            #low is now middle
            low = middle + 1
        
        else: 
            return middle

    return -1  # not found
