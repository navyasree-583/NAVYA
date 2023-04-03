# str1=input("enter the first string : ")
# str2=input("enter the second string : ")

# if(sorted(str1)==sorted(str2)):
#     print(f"{str1} and {str2} are anagrams")
# else:
#     print(f"{str1} and {str2} are not anagrams")

# Python3 program for the above approach
from collections import Counter
 
# function to check if two strings are
# anagram or not
def check(s1, s2):
   
    # implementing counter function
    print(Counter(s1))
    print(Counter(s2))
    if(Counter(s1) == Counter(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
 
 
# driver code
s1 = "listen"
s2 = "silent"
check(s1, s2)
