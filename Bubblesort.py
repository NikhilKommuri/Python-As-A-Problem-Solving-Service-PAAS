N = int(input())
list1 = []
for i in range(0,N):
    list1.append(int(input()))
    

def bubblesort(list1):
    for i in range(0,N):
        for j in range(0,N-i-1):
            if(list1[j+1] < list1[j]):
                list1[j+1],list1[j] = list1[j],list1[j+1]

bubblesort(list1)

print(*list1)
