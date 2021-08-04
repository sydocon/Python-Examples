
# Example file for working with date information

from datetime import date
from datetime import time
from datetime import datetime
def main():
    ## Date Objects
    # Get today's date from the simple today() method from the date class 
    today = date.today()
    print("Today's date is ", today)

    # print out the date's individual components
    print("Date components: ", today.day, today.month, today.year)

    # retrieve today's weekday (0= Monday)
    print("Today's weekday is: ", today.weekday())
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    print("Which is a ", days[today.weekday()])
    
    ## DateTime Objects
    # Get today's date from the datetime class
    today = datetime.now()
    print("The current day and time is: ", today)
    
    # Get the current time
    t = datetime.time(datetime.now())
    print(t)


if __name__ == "__main__":
    main()
    
# Prints :
# Today's date is  2021-08-04
# Date components:  4 8 2021
# Today's weekday is:  2
# Which is a  wed
# The current day and time is:  2021-08-04 17:09:51.545737
# 17:09:51.545765  
