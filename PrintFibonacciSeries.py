#Program to print x fibonacci Numbers

x = int(input())
fib0 = 0
fib1 = 1

for i in range(0,x):
    if (i==0):
        print(fib0)
    if (i==1):
        print(fib1)
    fib = fib0+fib1
    fib0 = fib1
    fib1 = fib
    if(fib<x):
        print(fib)
    
