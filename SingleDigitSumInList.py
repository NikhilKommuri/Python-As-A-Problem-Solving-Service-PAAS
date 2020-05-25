#Given a list find the sum of all the numbers till it becomes single digit

size = int(input())
list = []
sum = 0
for i in range(0,size):
    list.append(int(input()))
    sum = sum + list[i]

def digitsum(n):
    sum = 0
    while(n>0 or sum >9):
        if (n==0):
            n = sum 
            sum = 0
        
        sum = sum + n % 10
        n = n//10
    return sum

print(digitsum(sum))
