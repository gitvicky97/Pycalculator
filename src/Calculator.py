
import math

def add(a, b):
    a = float(a)
    b = float (b)
    c = a + b
    return c


def sub(a, b):
    a = float(a)
    b = float(b)
    c = b - a
    return c


def times(a, b):
    a = float(a)
    b = float(b)
    c = a * b
    return c


def div(a, b):
    a = float(a)
    b = float(b)
    c = b / a
    return c


def square(a):
    a = float(a)
    c = a * a
    return c


def sqrt(a):
    a = float(a)
    c = math.sqrt(a)
    return c


class calculator:
    result = 0

    def __init__(self):
        pass


    def addition(self, a, b):
        self.result = add(a, b)
        return self.result


    def subtraction(self, a, b):
        self.result = sub(a, b)
        return self.result


    def multiply(self, a, b):
        self.result = times(a, b)
        return self.result


    def division(self, a, b):
        self.result = div(a, b)
        return self.result


    def square_(self, a):
        self.result = square(a)
        return self.result


    def sqrt_(self, a):
        self.result = sqrt(a)
        return self.result