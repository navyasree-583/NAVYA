str1 = input("Enter the string 1")
st=str1
str2 = str1[::-1]
#str2 =''.join(reversed(str1))
print(str2)

if (str2 == st):
    print (f"{st} and {str2} are palindromes")
else:
    print(f"{st} and {str2} are not palindromes")