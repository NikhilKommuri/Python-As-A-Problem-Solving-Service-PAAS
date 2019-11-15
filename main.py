def centuryFromYear(year):
    rem =  year%100
    quo =  int(year/100)
    if(rem == 0):
        return quo
    else:
        return quo + 1
        
centuryFromYear(1905)  
