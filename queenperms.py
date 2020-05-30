def queensPermutation(boxes,tq,qpsf,path):
    if qpsf == tq:
        print(path)
        return
    for i in range(len(boxes)):
        if boxes[i] == False:
            boxes[i] = True
            queensPermutation(boxes,tq,qpsf+1,path+"q"+str(qpsf+1)+"b"+str(i)+" ")
            boxes[i] = False

n = 4
boxes = [False] *n
queensPermutation(boxes,2,0," ")
