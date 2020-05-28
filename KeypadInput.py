#Given a Mobile Keypad find all the possible words that can be formed using the 
#input to a keypad

keypadlist = ["","abc","def","ghi","jkl","mno","pqr","st","uvwx","yz"]

print(keypadlist)

def specialKeypad(s) -> [str]:
    if len(s) ==  0:
        return [" "]
    ch = s[0]
    rest = s[1:]
    recResult = specialKeypad(rest)
    myResult = []
    code = keypadlist[int(ch)]
    for s1 in recResult:
        for ch1 in code:
            myResult.append(ch1+s1)
    return myResult

print(specialKeypad("79"))
