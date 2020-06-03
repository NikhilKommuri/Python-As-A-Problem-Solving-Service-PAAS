#Rotate an Array k times 

nums = [1,2,3,4,5,6,7]
k =10

#Naive Approach
def rotatearray(nums,k):
    n = len(nums)
    while(k>0):
        for i in range(0,n):
            temp = nums[i]
            nums[i] = nums[n-1]
            nums[n-1] = temp
        k = k-1
    return  nums


#optimized Approach

def rotateArray(nums,k):
    if k > len(nums):
        k = k % len(nums)
    reverse(nums,0,len(nums)-k-1)
    reverse(nums,len(nums)-k,len(nums)-1)
    reverse(nums,0,len(nums)-1)
    print(nums)

def reverse(nums,i,j):
    while(i<j):
        nums[i],nums[j] = nums[j],nums[i]
        i += 1
        j -= 1

#rotateArray(nums,k)
