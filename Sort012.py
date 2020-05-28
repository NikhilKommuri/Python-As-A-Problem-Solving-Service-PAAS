'''
Sort Colors - Segregate 0,1,2

sort the array so that all the colors are adjacent to each other
example while red and blue are 0 , 1, 2 respectively

input [2,0,2,1,0,1]

output [0,0,1,1,2,2]

'''
arr = [2,0,2,1,1,0]

def sortcolors012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while(mid <= high ):
        if arr[mid] == 1:
            mid += 1
        elif arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -= 1
    print(arr)

sortcolors012(arr)
