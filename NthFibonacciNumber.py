#Program to Find the Nth Fibonacci Number
x = int(input())
fib = 0
fib0= 0
fib1= 1
if x == 0:
    fib = 0
elif x ==1:
    fib = 1
else:
    for i in range(1,x):
        fib = fib0 + fib1
        fib0 = fib1
        fib1 = fib
print(fib)
