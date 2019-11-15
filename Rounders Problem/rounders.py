def rounders(n):
    numlist = list(str(n))
    revlist = numlist[::-1]
    length = len(numlist)
    print("Length of the list",length)
    for i in range(length-1):
        if (int(revlist[i])>=5):
            print("if1",revlist[i+1]) 
            revlist[i]=0
            revlist[i+1]= int(revlist[i+1])+1
            print("if2",revlist[i+1])
        else :
            print("else",revlist[i]) 
            revlist[i]=0
        print(revlist[i])   
    print(n)
    numlist = revlist[::-1]
    x = int("".join(map(str, numlist)))
    print("After Rounding",x)  
rounders(4556)