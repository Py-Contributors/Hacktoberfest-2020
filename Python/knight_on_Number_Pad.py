#!/usr/bin/python3
"""
By Satyam Rai


Usage:

    $ python3 knight_on_Number_Pad.py     

    Or 

    $ python3 knight_on_Number_Pad.py n

    Or

    $ python3 knight_on_Number_Pad.py s n 

    s: starting Number (default 1)
    n: noOfHops  (default 3)



Problem :


        1   2   3
        4   5   6
        7   8   9
            0   
    
    Given s : Initial position of a Knight on a cell phone number pad [0-9]
    Given n : no of hops the knight makes
    If the initial placement of the knight is also considered Find the no of distinct numbers the knight will be able to dial..
    
    Eg :  s = 1  n = 2
    =>       1
           // \\            --- Hop 1
          8     6
        //\\  // \\ \\       --- Hop 2
        1 3   1  7  0

        Thus no of Distinct Numbers = 5


Three ways To solve the problem in order of increasing eficiency..

"""

# A global dict to store the neighbors
n_map = {
    1:(8,6)
    ,2:(7,9)
    ,3:(8,4)
    ,4:(3,9,0)
    ,5:()
    ,6:(1,7,0)
    ,7:(2,6)
    ,8:(1,3)
    ,9:(2,4),
    0:(4,6)
}

g_n_map = {}



#-------------------------------1---------------------
# Recursive Soln... Max n -> 998 on ubuntu 20.04 
def give_n(s,n):
    if n==0:
        return 1
    elif n==1:
        return len(n_map[s])
    else:
        nei = n_map[s]
        total = 0
        for _n in nei:
            if (_n,n-1) in g_n_map:
                temp = g_n_map[(_n,n-1)]
            else:
                temp = give_n(_n,n-1)
                g_n_map[(_n,n-1)]=temp
            total+=temp
        return total


#------------------2--------------------
#Iterative Soln1  (ineficient memory usage..)
table = None
import numpy as np
from queue import Queue
def give_n_iter(s,n):

    #util function
    def fill_table(s,n):
        if s==5:
            return 1
        global table
        val = table[s,n] 
        
        if (val== 0):
            neighbours = n_map[s]
            tot = 0
            for n_s in neighbours:
                tot += table[n_s,n-1]
            table[s,n] = tot
            return s
        else:

            return val
    

    if n==0 :
        return 1
    
    
    if n == 1 :
        return len(n_map[s])

    #init table..
    curQ = Queue()
    curQ.put(s)
    global table
    table = np.zeros((10,n+1),dtype = object)
    for i in range(10):
        table[i,0] = 1
        table[i,1] = len(n_map[i])

    for i in range(1,n+1):
        for j in range(0,10):
            fill_table(j,i)

    print(table[s,n])
    print(f"Size of array : {table.size* table.itemsize}")









#-----------------3 -----------------------
#   """Most Effiecient among these"""
# Iterative soln..
def noOfDistinctNos(startingNo,noOfHops):

    prevCount = [1]*10
    currCount = [0]*10
    currHops = 0
    while currHops < noOfHops:
        currCount = [0]*10
        
        #for each no
        for i in range(10):

            for neighbour in n_map[i]:                   

                currCount[i] += prevCount[neighbour]
        currHops+=1
        prevCount = currCount

    return currCount




# driver..
if __name__ == "__main__":
    import time
    import sys
    if len(sys.argv) > 2:
        s = int(sys.argv[1])
        n = int(sys.argv[2])
    elif len(sys.argv)>1:
        n = int(sys.argv[2])
        s=1
        print(f"Using default Values starting No: {s}  hops:{n}")
    else:
        s=1
        n = 3
        print(f"Using default Values starting No: {s}  hops:{n}")

    start = time.time()
    ans = noOfDistinctNos(s,n)              #Testing only most efficient one..

    print(f"noOfDistinctNos({s},{n})  = {ans[s]}",)
    print(f"For all s : {ans}")
    print(f"took {time.time()-start} seconds")

#AUTHOR : Satyam Rai
