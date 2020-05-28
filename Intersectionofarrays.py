#Intersection (No duplicates).
#Take as input N, the size of an array. Take N more inputs and store that in an array.
#Take N more inputs and store that in another array.
#Write a function which returns the intersection of two arrays (Duplicated are not allowed, Output is sorted).
#
#Ex.: For [1, 4, 5, 6, 7] and [10, 15, 7, 19, 6] the output will be [6, 7].

N = int(input())
list1 = []
list2 = []
for i in range(0,N):
    list1.append(int(input()))
for i in range(0,N):
    list2.append(int(input()))

set1 = set()
for x in list1:
    set1.add(x)
set2 = set()
for x in list2:
    set2.add(x)

list3 = []

for x in set1:
    if x in set2:
        list3.append(x)

print(*list3)
