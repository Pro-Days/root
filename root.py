import math



def root1():
    global x
    x = int(input())
    x = 1/2*x + 1/2 * 2/x

def root():
    root1(), root1(), root1(), root1(), root1()
    print(x)