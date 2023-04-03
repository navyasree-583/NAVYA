year=int(input("Enter the year"))
month=int(input("Enter the month"))
li=[1,2,3,5,7,8,10,12]

if(year%4==0 or year%100!=0 and year%400==0 ):
    leap=1
