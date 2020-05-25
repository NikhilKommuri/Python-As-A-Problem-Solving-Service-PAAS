#Finding the maximum number in an array

size = int(input())
list = []
max = 0
for i in range(0,size):
    list.append(int(input()))
    if(list[i]>max):
        max = list[i]
print(max)
