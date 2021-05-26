from System import Array
import os
import sympy

arr = Array[int](5)
for i in range(0, len(arr)):
    arr[i] = i

def hello(name):
    return "Hello " + name + "!"

class Dog:
    def __init__(self, name):
        self.name = name
    def walk(self, distance):
        return "Walking " + self.name + " " + str(distance) + " miles!"