def linear_search(values,target):
    n = len(values)
    for i in range(0, n):  
        if (values[i] == target):  
            return i  
    return -1

def binary_search(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, high, target)
 
    else:
        return -1
    

