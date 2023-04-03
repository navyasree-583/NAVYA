

year=int(input("Enter the year : "))

def check_leap(year):
    if(year%4==0 and year%100!=0):
        print(f"The year {year} is a leap year")
    elif(year%400==0 and year%100==0):
        print(f"The year {year} is a leap year")
    else:
        print(f"Year {year} is not a leap year")
check_leap(year)
