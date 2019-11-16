def adjacentElementsProduct(inputArray):
    maxproduct = inputArray[0] * inputArray[1]
    for i in range(0,len(inputArray)-1):
        product = inputArray[i] * inputArray[i+1]
        if(product >= maxproduct):
            maxproduct = product
            print("Max Product",maxproduct)
    return maxproduct    
        