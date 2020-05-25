#Given Two Arrays(Lists) Find the Sum of those Lists Just like how you would calulate sum of two Numbers
#E.g.:
#     [1, 0, 2, 9]
#+ [3, 4, 5, 6, 7]
#----------------------
#   [3, 5, 5, 9, 6]


N = int(input())
list1 = []
for i in range(0,N):
    list1.append(int(input()))
M = int(input())
list2 = []
for i in range(0,M):
    list2.append(int(input()))
result = []

if(M>N):
    a = M-N
    list1 = a * [0] + list1
elif(M<N):
    a = N-M
    list2 = a * [0] + list2

for i in range(len(list1)-1,-1,-1):
    sum = list1[i] + list2[i]
    if(sum <= 9):
        result.append(sum)
    else:
            sum = sum % 10
            result.append(sum)
            if(i!=0):
                list1[i-1] = list1[i-1] + 1
            else:
                result.append(1)

print(*result[::-1])
