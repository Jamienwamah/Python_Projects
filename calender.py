import sys
location = sys.path
print(location)

for i in location:
    print(i)


import calendar

leapdays = calendar.leapdays(2000, 2030)
print(leapdays)

isitleap = calendar.isleap(2036)
print(isitleap)