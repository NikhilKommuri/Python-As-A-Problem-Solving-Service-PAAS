#Given a Number and a digit the function that counts number of occurences of that digit in that number

n = int(input())
digit = int(input())

def digitconunter(n):
    count = 0
    while (n>0):
        digit_of_n = n % 10
        if(digit == digit_of_n):
            count = count + 1
        n = n // 10
    return count

print(digitconunter(n))
