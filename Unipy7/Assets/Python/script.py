from System import Array
import numpy as np
import sympy as sym
import scipy.integrate as scint

def getArrayOfSize(num):
    arr = Array[int](num)
    for i in range(0, len(arr)):
        arr[i] = i
    return arr

def getSumOfArray(arr):
    return sum(arr)

def exponent(num1, num2):
    return int(np.power(num1, num2))

def sin(num):
    return float(sym.sin(num))

def f(x):
    return 2 * x + 5

def integrate(low, high):
    return float(scint.quad(f, low, high)[0])

def hello(name):
    return "Hello " + name + "!"

class Dog:
    def __init__(self, name):
        self.name = name
    def walk(self, distance):
        return "Walking " + self.name + " " + str(distance) + " miles!"