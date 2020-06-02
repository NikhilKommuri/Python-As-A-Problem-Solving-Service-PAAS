# Given a string determine if a permutation of a string can be palindrome or not
# Ex: "aab" is input string one of perms is aba is a palindrome so function should return True 

def palindromicPermutation(s):
    myset = set()
    for ch in s:
        if ch in myset:
            myset.remove(ch)
        else:
            myset.add(ch)
    return  len(myset) <= 1

s = "aabf"
print(palindromicPermutation(s))
