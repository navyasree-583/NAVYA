import cmath

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

eq=((b**2)-4*a*c)
sq=cmath.sqrt(eq)

root1 = -b+sq/(2*a)
root2 = -b-sq/(2*a)

print(f"The roots of the quadratic equation are {root1} and {root2}")