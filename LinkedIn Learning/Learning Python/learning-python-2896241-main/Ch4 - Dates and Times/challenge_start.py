# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
# which day of week do you want to count, enter year & month, there are # of those days in the month and year specified
# sorry, that's not valid input, give list again
# docs for month calendar
import calendar

def countdays(year, month, whichday):
    daycount = 0
    weekslist = calendar.monthcalendar(year, month)
    for week in weekslist:
        if week[whichday] != 0:
            daycount += 1
    return daycount

def main():
    run = True
    while (run):
        try:
            print("Which day of the week do you want to count?")
            print("0: Monday")
            print("1: Tuesday")
            print("2: Wednesday")
            print("3: Thursday")
            print("4: Friday")
            print("5: Saturday")
            print("6: Sunday")
            print("Or 'exit' to quit")
            dayNum = input("Which day of the week do you want to count?")
            if dayNum == "exit":
                run = False
                break
            yearNum = input("Which year?")
            if yearNum == "exit":
                run = False
                break
            i = 0
            for name in calendar.month_name:
                print(i, name)
                i = i+1
            monthNum = input("Which month of the year do you want to count?")
            if monthNum == "exit":
                run = False
                break
        except Exception as e:
            print("Sorry, that's not valid input")
            print(e)

if __name__ == "__main__":
    main()