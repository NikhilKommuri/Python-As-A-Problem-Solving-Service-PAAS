#Function that returns only the integer part of the Square root 

n = int(input())

def sqrt(n):
    left = 0
    right = n + 1
    mid = (left + right) / 2
    projection = mid * mid
    while abs(projection - n) > 1e-13:
        if projection < n:
            left = mid
        else:
            right = mid
        mid = (left + right) / 2
        projection = mid * mid
    return int(mid)
    
print(sqrt(n))
