k=input("Enter any character : ")
print("The ascii value of " + k + " is ",ord(k))

k=input("Enter any string : ")
for i in k:
    ascii=ord(i)
    print(i," ",ascii)

num = int(input("enter the number : "))
print("The character value of num is ", chr(num))