#Abel Goshu
#1675552

print('Birthday Calculator')
print('Current day')
month1 = int(input('Month: '))
day1 = int(input('Day: '))
year1 = int(input('Year: '))
print('Birthday')
month2 = int(input('Month: '))
day2 = int(input('Day: '))
year2 = int(input('Year: '))
years = year1-year2-1
if(month2<month1):
    years+=1
elif(month1==month2):
    if(day2<day1):
        years+=1
if(month1==month2 and day1==day2):
    print('Happy Birthay')
print('You are '+str(years)+" years old.")