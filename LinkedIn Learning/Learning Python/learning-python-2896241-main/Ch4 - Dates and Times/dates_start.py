#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    # today = date.today()
    # print("Today's date is", today)

    # TODO: print out the date's individual components
    # print("Date components:", today.day, today.month, today.year)
    
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    # print("Today's weekday # is", today.weekday())
    # days = ["M", "T", "W", "R", "F", "Sa", "Su"]
    # print("Which is a ", days[today.weekday()])
    
    # TODO: retrieve tomorrow's weekday
    # today=date.today()
    # days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # print("Tomorrow will be " + days[(today.weekday()+1) % 7])

    # TODO: alert the user if their password expires in less than 7 days
    # if ((texp-date.today()).days < 7):
    # print("password will expire soon!")

    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is", today)
    
    # TODO: Get the current time
    t = datetime.time(datetime.now())
    print("The current time is", t)

  
if __name__ == "__main__":
    main()
  