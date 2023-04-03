num = int(input("enter the number"))

sum =0
temp=num
while(temp>0):
    rem=temp%10
    sum+=rem**3
    temp=temp//10
if(num==sum):
    print(f"The number {num} is a amstrong number")
else:
    print(f"The number {num} is not a amstrong number")