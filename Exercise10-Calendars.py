# Example file for working with Calendars



# import the calendar module
import calendar

# create a plain tect calendar
c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2021,1,0,0)
print(st)

# create a HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.MONDAY)
st = hc.formatmonth(2021,1)
print(st)

# loop over the days of the month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2021,1):
    print(i)

# The Calendar module provides useful utilities for the given locale, 
# such as the names of the days and months in both full and abbrievated forms
for name in calendar.month_name:
    print(name)
    
for day in calendar.day_name:
    print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on: ")
for m in range(1,13):
    cal= calendar.monthcalendar(2021,m)
    weekone= cal[0]
    weektwo= cal[1]
    
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    
    print("%10s %2d" % (calendar.month_name[m], meetday))



