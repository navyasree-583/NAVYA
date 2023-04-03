year = input("Enter the year : ")
month = int(input("Enter the month : "))
l=len(year)
x=[4,6,9,11]
y=[1,3,5,7,8,10,12]
if(l==4 and (month>=1 and month<=12)):
    if month in x:
        print(f"There are 30 days")
    elif month in y:
        print(f"There are 31 days")
    else:
        if(int(year)%4==0 and int(year)%100!=0 or int(year)%400==0):
            print(f"There are 29 days")
        else:
            print(f"There are 28 days")
else:
    print("Wrong input")
            

