#Given an array with elements 0 to N-1 and an element that is repeated only once find the duplicate element
size = int(input())
list = []
sum = 0
totalsum = 0
for i in range(0,size):
    list.append(int(input()))
    totalsum = totalsum + list[i]
for i in range(0,size-1):
    sum = sum + i

print(totalsum - sum)
