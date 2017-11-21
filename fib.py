# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:29:06 2017

@author: MFP53502
"""

def __fib(n):
    if(n<2):
        return 1
    else:
        return __fib(n-1)+__fib(n-2)
    
    
def fib_n_series(N):

    cnt = 1
    while cnt <= N:
        print(__fib(cnt))
        cnt += 1
        
fib_n_series(10)



def stair(n):
    if(n<4):
        numSolution = [0,1,2,4]
        return numSolution[n]
    else:
        return(stair(n-3) + stair(n-2) + stair(n-1))
    
n = 10
print(stair(n))    

n = 2
def get_mod_fib(n):
    f1, f2, f3 = 1, 2, 4
    for i in range(n-1):
        f1, f2, f3 = f2, f3, f1 + f2 + f3
        print(f1,f2,f3)
    return f1

print(get_mod_fib(n))

def stair(n):
    numSolution = [0,1,2,4]
    for i in range(n+1):
        if(i >= 4):
            val = numSolution[i-3] + numSolution[i-2] + numSolution[i-1]
            print("var%d"%val)
            numSolution.append(val)
    return(numSolution[n])
print(stair(7))