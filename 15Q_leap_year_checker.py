def leap_year(year):
    #A leap year is called when the year is divisible by 4 and not divisible by 100
    if (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

def main():
    while True:
        year = int(input("Enter a year to check (or 0 to quit): "))
        if year==0:
            break
        else:
            if leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
main()