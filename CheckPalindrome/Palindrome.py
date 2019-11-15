def checkPalindrome(inputString):
    length = len(inputString)
    inputlist = list(inputString)
    if (length%2==0):
        for i in range(0,length/2):
            print(inputlist[i])

checkPalindrome("abbabba")   