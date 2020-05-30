def queensCombination(boxes,tq,qpsf,path,lqp):
    if qpsf == tq:
        print(path)
        return
    for i in range(lqp+1,len(boxes)):
        if boxes[i] == False:
            boxes[i] = True
            queensCombination(boxes,tq,qpsf+1,path+"q"+str(qpsf+1)+"b"+str(i)+" ",i)
            boxes[i] = False

n = 4
boxes = [False] *n
queensCombination(boxes,2,0," ",-1)
