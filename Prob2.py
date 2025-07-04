"""
Define a recursive function to compute the values of PMF and CDF of "EX16" in Random Variables. Meanwhile, you need to plot its PMF and CDF with bar chart by using Matplotlib.
If you are not familiar with Python, especially in defining a recursive function or plot a data, then you may watch my teaching videos.
1) Define a function: https://youtu.be/VSKMB-vwpd8
2) Visualization: https://youtu.be/xiSOQiqIJrY
"""
import numpy as np
import matplotlib.pyplot as plt

def recursiveFactorial(n):
    if n == 0: return 1
    else: return n * recursiveFactorial(n - 1)

def C(n, k):
    return recursiveFactorial(n) // recursiveFactorial(k) // recursiveFactorial(n - k)

def arrInitFloat(num, low, high):
    if low > high:
        return None
    else:
        a = high - low
        b = high - a
        out = (np.random.rand(num) * a + b).tolist()
        out = np.array(out)
        return out

### PMF
def recursivePMF(p, n, k):
    if k == 0: return ((1 - p) ** n)
    else: return (p / (1 - p)) * ((n - k + 1) / k)* recursivePMF(p, n, k - 1)

def recursiveAddPMF(p, n, k, arr):
    if k <= n:
        x = arr[k]
        arr[arr == x] = recursivePMF(p, n, k)
        arr = recursiveAddPMF(p, n, k + 1, arr)
    return arr

### CDF
def recursiveCDF(arr, n, k):
    if k <= n: return arr[k] + recursiveCDF(arr, n, k + 1)
    else: return 0

def recursiveAddCDF(p, n, k, arr):
    if k <= n:
        arr[k] = arr[k - 1] + arr[k]
        arr = recursiveAddCDF(p, n, k + 1, arr)
    return arr

### PMF and CDF
def PMFandCDF(p, n, k):
    PMF = arrInitFloat(n + 1, 2, 3) ### initialize: create (n + 1) random float between 2 and 3
    PMF = recursiveAddPMF(p, n, k, PMF) ### get PMF
    CDF = PMF.copy() ### initialize: deep copy PMF to CDF
    CDF = recursiveAddCDF(p, n, k + 1, CDF) ### get CDF
    ### visualize
    print("PMF:", PMF)
    print("CDF:", CDF)
    draw(PMF, CDF)
    return None

### draw
def draw(PMF, CDF):
    x = np.array([0, 1, 2, 3, 4, 5, 6])
    x2 = np.array([-0.2, 0.8, 1.8, 2.8, 3.8, 4.8, 5.8])
    y = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    h = PMF
    h2 = CDF
    plt.bar(x, h, color = 'b', width = 0.4, label = 'PMF', align = 'edge')
    plt.bar(x2, h2, color = 'r', width = 0.4, label = 'CDF')
    plt.title('EX16 PMF and CDF from 0 to 6')
    plt.xlabel('X')
    plt.ylabel('PMF and CDF')
    plt.legend(loc = 'upper left')
    plt.show()
    return None

### main running
PMFandCDF(0.4, 6, 0)