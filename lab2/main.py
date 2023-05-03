from random import sample
from sort import InsertionSort, MergeSort
from time import time_ns

def run(n):
    data = sample(range(1,n+1),n)
    start_time = time_ns()
    InsertionSort(data)
    end_time = time_ns()
    time_taken = end_time-start_time
    print(f"time_taken for InsertionSort is {time_taken}")
    
    # print(data)

    start_time = time_ns()
    MergeSort(data,0,n-1)
    end_time = time_ns()
    time_taken = end_time-start_time
    print(f"time_taken for Merge is {time_taken}")

if __name__ =='__main__':
    run(10000)