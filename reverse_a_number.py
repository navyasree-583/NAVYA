num = int(input("enter the number"))
rev=0
while(num>0):
    rem =num%10
    rev =rev*10+rem
    num=num//10

print(f"The reverse number is {rev}")