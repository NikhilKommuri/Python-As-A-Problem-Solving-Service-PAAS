#searching for a number using binary search algorithm

N = int(input())
list = []
for i in range(0,N):
    list.append(int(input()))
num = int(input())

def searchNumber(list,num):
    left = 0
    right = N-1
    while(left<=right):
        mid = left + (right-left)//2
        if(list[mid] == num):
            return mid
        elif(list[mid] < num):
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(searchNumber(list,num)) 
