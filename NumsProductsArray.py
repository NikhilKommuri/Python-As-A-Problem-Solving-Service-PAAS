#Product of all numbers in array except number itself , withour using the division method

nums = [1,2,3,4]

def productofArray(nums):
    n = len(nums)
    left = [0] * n
    right = [0] * n
    left[0] = 1
    right[n-1] = 1
    for i in range (1,n):
        left[i] = left[i-1] * nums[i-1]
    for i in range(len(nums)-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]
    res = [0] * n
    for i in range(n):
        res[i] = left[i] * right[i]
    return res

#print(productofArray(nums))

# Optimized Version

def productofArray2(nums):
    n = len(nums)
    res = [0] * n
    res[0] = 1
    for i in range(1,n):
        res[i] = res[i-1] * nums[i-1]
    temp = 1
    for i in range(n-2,-1,-1):
        res[i] = res[i] * nums[i+1] * temp
        temp = temp * nums[i+1]
    return res
#print(productofArray2(nums))
