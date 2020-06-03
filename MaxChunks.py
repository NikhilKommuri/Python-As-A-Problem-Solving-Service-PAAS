#Max Chunks to Make Sorted

arr = [1,0,2,3,4]
def maxChunks(arr):
    res = 0
    maximum = 0
    for i in range(0,len(arr)):
        maximum = max(maximum,arr[i])
        if maximum == i:
            res = res + 1
    return res

print(maxChunks(arr))
