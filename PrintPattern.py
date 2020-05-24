#Print the following pattern when you give input as 4

#1
#2 3
#4 5 6
#7 8 9 10



x = int(input())
number = 1
for i in range(0, x):
    for j in range(0, i + 1):
        if (j != i):
            print(number, end=" ")
            number = number + 1
        else:
            print(number, end="")
            number = number + 1

    print("\r")
