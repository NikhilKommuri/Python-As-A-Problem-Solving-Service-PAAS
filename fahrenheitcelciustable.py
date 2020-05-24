#Given range of fahrenheit temperature and the increment number the function that returns the fahrenheit and celcus in that range

start = int(input())
end = int(input())
step = int(input())

def fahrceltable(start,end,step):
    for i in range(start,end+1,step):
        fahrenheit = i
        celcius = int((5/9) * (fahrenheit-32))
        print(fahrenheit,":",celcius)

fahrceltable(start,end,step)
