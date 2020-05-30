#Is mirror inverse?
#Take as input N, the size of an array. Take N more inputs and store that in the array.
#Write a function that returns "Yes" if the array is mirror-inverse and "No" otherwise.

#A number is called mirror-inverse if its inverse is equal to itself.
#Make sure you call the function from question "Inverse of an array" in order to find the inverse in this function.

#Input Format
#Number N (Size Of The Array)
#Array Elements(One Element/Line)

N = int(input())
list1 = []
for i in range(0,N):
    list1.append(int(input()))
list2 = N * [-1]

def inverseofarray(list1):
    num = 1
    for x in list1:
        list2[x-1] = num
        num = num + 1
        
inverseofarray(list1)

def isinverse(list1,list2):
    for i in range(0,N):
        if(list1[i]!=list2[i]):
            return "No"
        else:
            return "Yes"

print(isinverse(list1,list2))
    
