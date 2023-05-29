#     here in this code:
#     the function return an array of strings that represent binary number from 0 to 2^n
#     bin funtion gives binary value of the input number with initial 2 character being 0b
#     to remove 0b, we slice the value with[2:]
#     rjust adds padding to left until there are n characters 

def get_strings(n):
    strings = []
    for x in range(2**n):
        strings.append(bin(x)[2:].rjust(n, '0'))
    return strings


def Brute_Force_01Knapsack(p,w,m):
    assert len(p) == len(w)     # here p and w are array of weights and profit whose number should be equal
    n = len(p)
    bit_strings = get_strings(n)
    maxProfit = 0
    solution = ''
    for s in bit_strings:
        profit = sum([int(s[i]) *p[i] for i in range(n)] )
        weight = sum([int(s[i])* w[i] for i in range(n)] )
    
        if weight <= m and profit > maxProfit:
            maxProfit = profit
            solution = s

    return(solution,maxProfit)
 
def Brute_Force_fractionalKnapsack(p,w,m):
    assert len(p) == len(w)     
    n = len(p)
    bit_strings = get_strings(n)
    maxProfit = 0
    
    for s in bit_strings: #checking for each combination of binary strings
        weight = 0
        profit = 0
        for i in range(n): # for each item in a singke combination
            if(s[i]== '1'):
                if w[i]<= m - weight:
                    profit += p[i]
                    weight += w[i]
                else:
                    fracprofit = (m-weight)/w[i]*p[i]
                    profit = profit + fracprofit
                    weight = m
            
            if profit > maxProfit:
                maxProfit = profit
    return maxProfit                   

def Greedy_fractionalKnapsack(p,w,m):
    assert len(p) == len(w)   
    items = [(value, weight) for value, weight in zip(p, w)]
    items.sort(key=lambda x: x[0] / x[1], reverse=True) # Sort items based on value-to-weight ratio
    profit = 0
    remaining_capacity = m       
    for value, weight in items:
        if weight <= remaining_capacity:
            # Add the entire item to the knapsack
            profit += value
            remaining_capacity -= weight
        else:
        # Add a fraction of the item to the knapsack
            fraction = remaining_capacity / weight
            profit += fraction * value
            break # No more items can be added
    return profit