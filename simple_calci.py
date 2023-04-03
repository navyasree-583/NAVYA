from math import floor


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mod(a,b):
    return a%b
def mul(a,b):
    return a*b
def div(a,b):
    return floor(a/b)

print("Select a operation")
print("a.ADD")
print("b.SUB")
print("c.MOD")
print("d.MUL")
print("e.DIV")
print("Select a chioce from (a/b/c/d/e)")
ch=input("Enter your choice : ")

a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))

if ch=='a':
    print(f"Addition of numbers {a} and {b} is ",add(a,b))
elif ch=='b':
    print(f"Subtraction of numbers {a} and {b} is ",sub(a,b))
elif ch=='c':
    print(f"Modulo of numbers {a} and {b} is ",mod(a,b))
elif ch=='d':
    print(f"Multiplication of numbers {a} and {b} is ",mul(a,b))
elif ch=='e':
    print(f"Division of numbers {a} and {b} is ",div(a,b))


