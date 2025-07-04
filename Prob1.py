"""
Using Python programming, to proof "for any constants a and b: Var(aX+b)=a^2Var(X)"
You may try different a and b for calculating the variance in order to prove this.
"""
import numpy as np
import random

def Var(num):
    return np.mean(num * num) - np.mean(num) * np.mean(num)

x = 10
print("Let x =", x)
print("In Var(num), return np.mean(num * num) - np.mean(num) * np.mean(num)\n")
index = 0
for i in range(5): ## test 5 groups
    print("Test", i + 1)
    ### get 10 random constant in range (0, 1000) and transform to np.array()
    data1 = np.array(random.sample(range(0, 1000), 10))
    data2 = np.array(random.sample(range(0, 1000), 10))
    print("data 1:", data1)
    print("data 2:", data2)
    ### get data expectations
    a = np.mean(data1)
    b = np.mean(data2)
    print("a:", a)
    print("b:", b)
    ### proof
    left = Var(a * x + b)
    right = a * a * Var(x)
    print("Var(a * x + b):", left)
    print( "a * a * Var(x):", right)
    ### results
    if left == right: print ("Var(", a, "*", x, "+", b, ") ==", a, "*", a, "*", "Var(", x, "), Q.E.D.")
    else: print("Not equal, ERROR!")
    index = index + 2
    print("\n")