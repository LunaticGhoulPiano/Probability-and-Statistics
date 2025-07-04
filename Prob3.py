import math
import sys
sys.setrecursionlimit(2000) ### set recursion depth

def Euler(average):
    ### Willing to slove the minimum floating point here ...
    return math.pow(math.exp(1), (-1 * average))

def Poisson(average, X):
    if X == 0: return Euler(average)
    return (average / X) * Poisson(average, X - 1)

def Sum(average, X):
    if X == 0: return Poisson(average, X)
    return Poisson(average, X) + Sum(average, X - 1)

print(Sum(100, 90))
print(Sum(1000, 1075))