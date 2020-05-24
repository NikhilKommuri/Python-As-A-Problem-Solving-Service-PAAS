#given a number replace all zero's with 5 in that number

x = int(input())

num = x
result = 0

decimalplace = 1

while(x > 0):
    digit = x % 10
    if(digit==0):
        result = result + (5*decimalplace)
    x = x // 10
    decimalplace = decimalplace * 10
    
print(num+result)
