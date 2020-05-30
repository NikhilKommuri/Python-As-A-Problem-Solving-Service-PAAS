N = int(input())
list1 = []
for i in range(0,N):
    list1.append(int(input()))

#print(*list1)
def selectionsort(list1):
    for i in range(0,N):
        min_place = i
        for j in range(i+1,N):
            if(list1[min_place]>list1[j]):
                min_place = j
        list1[min_place],list1[i] = list1[i],list1[min_place]


selectionsort(list1)

print(*list1)
                
