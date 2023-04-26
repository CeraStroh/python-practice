# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
# which day of week do you want to count, enter year & month, there are # of those days in the month and year specified
# sorry, that's not valid input, give list again
# docs for month calendar
import calendar

def main():
    run = True
    while (run):
        # try:
            days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
            i = 1
            for d in calendar.day_name:
                print(i, d)
                i = i+1
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
        # except ValueError as e:
        #     print("Sorry, that's not valid input")
        #     print(e)

if __name__ == "__main__":
    main()