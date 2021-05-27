from System import Array
import numpy as np

def getArrayOfSize(num):
    arr = Array[int](num)
    for i in range(0, len(arr)):
        arr[i] = i
    return arr

def exponent(num1, num2):
    return np.exp(num1, num2)

def hello(name):
    return "Hello " + name + "!"

class Dog:
    def __init__(self, name):
        self.name = name
    def walk(self, distance):
        return "Walking " + self.name + " " + str(distance) + " miles!"