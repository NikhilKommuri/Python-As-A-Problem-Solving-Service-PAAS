#Palindrome Using Lists


def checkPalindrome(inputString):
    length = len(inputString)
    inputlist = list(inputString)
    isPalindrome = False
    for i in range(0,length):
      if inputlist[i] == inputlist[length-1]:
        isPalindrome = True
        print(isPalindrome)
      else:
        isPalindrome = False
        print(isPalindrome)
          

checkPalindrome("abblnfbba")   