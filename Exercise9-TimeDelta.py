# Example file for working with timedelta objects

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days= 365, hours=5, minutes= 1))

# print today's date
now= datetime.now()
print("today is: "+ str(now))

# print today's date one year from now
print("One year from now it will be "+ str(now + timedelta(days= 365)))

# create a timedelta that uses more than one argument
print("In 2 days and 3 weeks it will be " + str(now + timedelta(days=2, weeks=3)))

# calculate the date 1 week ago, formatted as a string
t= datetime.now() - timedelta(weeks=1) 
s= t.strftime("%A %B %d, %Y")
print("One week ago it was "+ s)

### How many days until April Fool's day?
today= date.today()
afd= date(today.year, 4, 1)

# use date comparison to see if April Fool's day has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April Fool's Day already went by %d days ago" % ((today-afd).days))
    afd= afd.replace(year= today.year+1)
    
# Now calculate the amount of time until April Fool's Day
time_to_afd= afd-today
print("It's just ", time_to_afd.days,"days until April Fool's day")


# Prints:
# 365 days, 5:01:00
# today is: 2021-08-04 17:41:44.827040
# One year from now it will be 2022-08-04 17:41:44.827040
# In 2 days and 3 weeks it will be 2021-08-27 17:41:44.827040
# One week ago it was Wednesday July 28, 2021
# April Fool's Day already went by 125 days ago
# It's just  240 days until April Fool's day
