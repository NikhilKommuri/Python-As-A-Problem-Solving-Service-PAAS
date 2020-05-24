#Print This Pattern
#1
#2 2
#3 0 3
#4 0 0 4
#5 0 0 0 5


numRows=int(input())
count=1
for row in range (1, numRows+1) :
    s = ""
    for col in range (1, row+1) :
        if (col == 1):
            print(row,end=" ")
        elif(col == row):
            print(row,end="")
        else:
            print(0,end=" ")
    print("")
