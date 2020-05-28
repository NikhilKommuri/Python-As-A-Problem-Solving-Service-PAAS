'''
Target Sum Subset
Given Non -ve integers print subsets of given set equals to target

Ex : set is {10,20,30,40,50}

target = 30

output =

[10,20]
[30]
'''

inputarr = [10,20,30,40,50,60,70]
target = 70

def targetsumsubset(arr,target,vidx,subset,setSum):
    if vidx == len(arr):
        if setSum == target:
            print(subset)
        return
    targetsumsubset(arr,target,vidx+1,subset,setSum)
    targetsumsubset(arr,target,vidx+1,subset+str(arr[vidx])+" ",setSum+arr[vidx])

targetsumsubset(inputarr,target,0," ",0)
