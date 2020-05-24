#checking whether a number is power of 2 or not using the bitwise operators
#for all the numbers that are powers of 2 there be only one bit that is set to 1

x = int(input())

count=0

while(x):
    count += x & 1
    x >>= 1
    
if(count != 1):
    print("No")
else:
    print("Yes")
    
