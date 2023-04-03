# numbers=(1,2,3,1,5,5,4,5,2)
# c=0
# for i in numbers:
#     if i==5:
#         c+=1
# print(c)

n="This is a python language for you"
str1=n.split(' ')
c=0
for i in str1:
    if len(i) %2 !=0:
        print(i)
    continue
    
a =[10,20]
b=a
b+=[30,40]
print(b)
    