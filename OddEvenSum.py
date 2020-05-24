#Sum of Odd and Even placed digits of a Number

x = int(input())
rev = 0
while x > 0:
    digit = x%10
    rev = (rev*10) + digit 
    x = x//10
oddsum = 0
evensum = 0
flag=0
while rev > 0:
    if (flag == 0):
        digit = rev%10
        oddsum = digit + oddsum
        rev = rev//10
        flag = 1
    if (flag == 1):
        digit = rev%10
        evensum = digit + evensum
        rev = rev//10
        flag = 0
print(oddsum)
print(evensum)
    
