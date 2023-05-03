from random import sample
from search import linear_search
from search import binary_search
from time import time_ns

def run(n):
    data = sample(range(1,n+1),n) #sample ([1,2,3,....])
    # start_time = time_ns()
    # linear_search(data,data[-1]) 
    # end_time = time_ns()
    # time_taken = end_time-start_time
    # print(f"time_taken for linear_search is {time_taken}")

    data.sort()
    start_time1 = time_ns()
    binary_search(data,0,int(n)-1,data[-1])
    end_time1 = time_ns()
    time_taken1 = end_time1-start_time1
    print(f"time_taken for binary_search is {time_taken1}")


if __name__ =='__main__':
    run(100000)
