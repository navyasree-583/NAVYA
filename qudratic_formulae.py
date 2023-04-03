import cmath

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))



def roots_are(a,b,c):
    eq = (b**2) - 4*a*c
    sq = cmath.sqrt(eq)

    if(eq>0):
        root1 = -b+sq/(2*a)
        root2 = -b-sq/(2*a)
        print("Roots are real and different")
        print("Root1 and Root2 of equations are {root1} and {root2}".format(root1,root2))
    elif(eq==0):
        roots = (-b/(2*a))
        print("Roots are equal")
        print(f"Roots of equations are {roots}")
    else:
        root1 = -b/(2*a)
        root2 = -b/(2*a)
        print("Roots are complex")
        print("Root1 is ",(-b/(2*a)),"+i",sq)
        print("Root1 is ",(-b/(2*a)),"-i",sq)

if(a==0):
    print("Enter a postive number")
else:
    roots_are(a,b,c)