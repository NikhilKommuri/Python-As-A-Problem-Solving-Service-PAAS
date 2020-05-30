#Inverse of an array.
#Take as input N, the size of an array. Take N more inputs (1 through N) and store that in the array.
#Write a function that returns the inverse of this array.

#Definition of inverse:
#Inverse of [5, 4, 1, 2, 3] is [3, 4, 5, 2, 1].
#In [5, 4, 1, 2, 3], “5” is at 1st place, therefore in [3, 4, 5, 2, 1], “1” is at 5th place.
#In [5, 4, 1, 2, 3], “4” is at 2nd place, therefore in [3, 4, 5, 2, 1], “2” is at 4th place.

N = int(input())
list1 = []
for i in range(0,N):
    list1.append(int(input()))
list2 = N * [-1]
num = 1
for x in list1:
    list2[x-1] = num
    num += 1

print(*list2)
