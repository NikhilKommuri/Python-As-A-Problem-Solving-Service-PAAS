#Given an Array Find the pairs in an array whose sum is equal to the target number

E.g.: For [3, 1, 9, 7, 5, -1] and target of 8 the output is 1 and 7, 3 and 5, 9 and -1.

N = int(input())
list = []
for i in range(0,N):
    list.append(int(input()))
target = int(input())

def mergesort(list):
    if len(list)>1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        mergesort(left)
        mergesort(right)
        list.clear()
        while(len(left)>0 and len(right) >0):
            if(left[0]<= right[0]):
                list.append(left[0])
                left.pop(0)
            else:
                list.append(right[0])
                right.pop(0)
        for i in left:
            list.append(i)
        for i in right:
            list.append(i)
mergesort(list)


left = 0
right = len(list) - 1

while(left < right):
    sum = list[left] + list[right]
    if (sum == target):
        print(list[left],list[right])
        left = left+1
        right = right-1
    elif(sum > target):
        right = right-1
    else:
        left = left+1

