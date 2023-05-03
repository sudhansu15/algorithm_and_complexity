import math

def InsertionSort(array):
    length = len(array)
    for j in range(1,length):
        key =  array[j]
        i = j-1
        while i>=0 and array[i]> key :
            array[i+1] = array[i]
            i= i -1
        array[i+1] = key
    return array

# newArray = InsertionSort([5,2,4,7,1,3,8,6])
# print(newArray)

def MergeSort(array,p,r):
    if p<r:
        q = math.floor((p+r)/2)
        MergeSort(array,p,q)
        MergeSort(array,q+1,r)
        Merge(array,p,q,r)
    return array
    
    
def Merge(A,p,q,r):
    n1 = q-p+1
    n2= r-q
    left = []
    right = []
    for i in range(n1):
        left.append(A[p+i])
    for j in range(n2):
        right.append(A[q+j+1])
    left.append(100000001)
    right.append(100000001)
    i =0
    j = 0
    for k in range(p,r+1):
        if left[i]<= right[j]:
            A[k] = left[i]
            i = i+1
        else:
            A[k]= right[j]
            j=j+1

# newArray = [5,2,4,7,1,3,8,6]
# MergeSort(newArray,0,7)
# print(newArray)

# secondArray = MergeSort([5,2,4,7,9,3,8,6],0,7)
# print(secondArray)

        

