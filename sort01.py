'''
Segregate 0's and 1's in an array
Given an array of integers segregate 0's to the LHS
and 1's to the RHS
Try to solve in Linear time

Eg: [0,1,0,1,1,0,0,1]

output = [0,0,0,0,1,1,1,1]
'''


#Approach1
arr = [0,1,0,1,0,0,1,1,1,0]
def segregate01(arr):
    left = 0
    right = len(arr)-1

    while(left<=right):
        if (arr[left] == 1):
            arr[left],arr[right] = arr[right],arr[left]
            right -=1
        else:
            left +=1
    print(arr)
segregate01(arr)

#Approach2
def sort01(arr):
    i = 0
    j = 0
    while(i<len(arr) and j<len(arr)):
        if arr[j] == 0:
            arr[i],arr[j] = arr[j],arr[i] #swapping the variables
            i += 1
            j += 1
        else:
            j+=1
    print(arr)

sort01(arr)
