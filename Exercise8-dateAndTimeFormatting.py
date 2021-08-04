# Example file for formatting time and date output

from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes
    now = datetime.now()

    ### Date formatting ###
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("The current year is: %Y"))
    print(now.strftime("The current month is: %b"))
    print(now.strftime("The current date of month is: %d"))
    print(now.strftime("%a, %d %B, %y"))
    
    # %c - locale's date and time, %x - locale's date, %X - locale's time 
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))

    ### Time formatting ###

    # %I/%H - 12/24 Hour, %M - minute, $S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24 hour time: %H:%M %p"))
    

if __name__ == "__main__":
    main()

# Prints:
# The current year is: 2021
# The current month is: Aug
# The current date of month is: 04
# Wed, 04 August, 21
# Locale date and time: Wed Aug  4 17:23:11 2021
# Locale date: 08/04/21
# Locale time: 17:23:11
# Current time: 05:23:11 PM
# 24 hour time: 17:23 PM
