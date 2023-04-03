num=int(input("Enter the number"))

def fact(num):
    f=1
    for i in range(0,num):
        f=f*(i+1)
    print(f"The factorial of {num} is ",f)
fact(num)