def leaptest(year):
    year = int(year)
    if year == 0:
        return 0
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

class func:
    def __init__(self):
        given_year = input("Enter a year to see if it's a leap year: ")
        value = leaptest(given_year)
        if value == 1:
            print("The given year is a leap year")
        else:
            print("The given year is not a leap year")

if __name__ == "__main__":
    prompt = func()