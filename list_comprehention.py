# print("Hello!")

# ls= [i for i in range(100) ]
# print(ls)

# dict1={i:f"Item {i}" for i in range(5)}
# print(dict1)

# dict2={value: key for key,value in dict1.items()}
# print(dict2)

num = int(input("How many elements you want to add: "))
input_elements = input("Enter elements separated by space: ")
List = input_elements.split()

choice = input('''
Which type of Comprehension you want to create?
A. For List Comprehension
B. For Dictionary Comprehension
C. For Set Comprehension
D. For Generator Comprehension

-->  
''')
if choice == 'A':
    list1 = [a for a in List]
    print(list1)
    print(type(list1))

elif choice == 'B':
    Dict1 = {a : f" Item{a} " for a in List}
    print(Dict1)
    print(type(Dict1))

elif choice == 'C':
    Set1 = {a for a in List}
    print(Set1)
    print(type(Set1))

elif choice == 'D':
    Generator1 = (a for a in List)
    print(Generator1)
    print(type(Generator1))
else:
    print("Invalid Input!")
