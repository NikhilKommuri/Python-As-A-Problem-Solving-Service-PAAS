'''
You are given N, and for a given N x N chessboard, find a way to place N queens such that no queen can attack any other queen on the chess board. A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens. You have to print all such configurations.
'''
def nqueens(chess,qpsf,path,lqp):
    if qpsf == len(chess):
        print(path)
        return
    for i in range(lqp+1,len(chess) * len(chess)):
        row = int(i/len(chess))
        col = int(i%len(chess))
        if chess[row][col] == False:
            if (isQueenSafe(chess,row,col)):
                chess[row][col] = True
                nqueens(chess,qpsf+1,path+"q"+str(qpsf+1)+"b"+str(i)+" ",i)
                chess[row][col] = False

def isQueenSafe(chess,row,col):
    directions = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]
    for d in range(len(directions)):
        dist = 1
        while(True):
            enemyrow = row + dist * directions[d][1]
            enemycol = col + dist * directions[d][0]
            if enemyrow < 0 or enemycol < 0 or enemyrow >= len(chess) or enemycol >= len(chess):
                break
            if chess[enemyrow][enemycol] == True:
                return False
            dist += 1
    return True

chess = [
    [False,False,False,False],
    [False,False,False,False],
    [False,False,False,False],
    [False,False,False,False]
]
nqueens(chess,0," ",-1)
