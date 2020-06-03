#Find the continous subarray with maximum sum

arr = [-3,-4,-1]
def maxsumsubarray(arr):
    local_max_sum = 0
    global_max_sum = -999999
    for i in range(0,len(arr)):
        local_max_sum = max(arr[i],arr[i]+local_max_sum)
        if(local_max_sum>global_max_sum):
            global_max_sum = local_max_sum
    return  global_max_sum

#print(maxsumsubarray(arr))

'''
Another Way to do it but only for +ve sum
nums = [-2,-3,4,-1,-2,1,5,-3]
def kadane(nums):
    csum = nums[0]
    osum = nums[0]
    for i in range(1,len(nums)):
        csum = csum + nums[i]
        if csum < 0:
            csum = 0
        osum = max(osum,csum)
    return osum
#print

'''
