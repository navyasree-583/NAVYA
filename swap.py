def swap(a,b):
    temp=a
    a=b
    b=temp
    print("The value of a is = ",a)
    print("The value of b is = ",b)
a=int(input("Enter value of a"))
b=int(input("Enter value of b"))

swap(a,b) 

# without third variable
a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
a=a+b
b=a-b
a=a-b
print("The value of a is = ",a)
print("The value of b is = ",b)


