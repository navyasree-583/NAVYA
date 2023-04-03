# num=int(input("enter the number"))

# sqrt = num ** (1/2)
# print(int(sqrt))


num=int(input("Enter the number : "))
max=num
min = 0

for i in range(10):

    middle=(max+min)/2
    sq_val = middle ** 2
    if(sq_val==num):
        break
    max=middle
    min=middle

print(f"The square root of number {num} is {middle}")

# number = 9

# # initializing minimum value as 0
# minimum = 0

# # initializing maximum value with input number
# maximum =number

# # repeating the loop 10 times using for loop
# for i in range(10):
#    # getting the middle value
#    middle =(minimum+maximum)/2
#    # getting the square of the middle value
#    squareValue=middle**2
#    # checking whether the square value of the middle value is equal to the number
#    if squareValue ==number:
#       # break the code if the condition is true
#       break
#    # checking whether the square value of the middle value is more than the number
     
#    # taking max value as the middle value if the condition is true
#    maximum=middle
  
#    # else if the square value of the middle value is less than the number
#    # taking the min value as a middle
#    minimum=middle

# # printing the middle value which is the resultant square root
# print("The resultant square root of", number, "=", middle)



