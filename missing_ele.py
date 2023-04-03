len = int(input("Enter the len val"))
summ=0
while(len>0):
    summ+=len
    len=len-1
arr1=[1,2,3,4,5,7,8,9,10]
summ2=0
arrlen=len(arr1)
print(arrlen)
for i in range (0,arrlen):
    summ2+=arr1[i]

print('missing element is ', summ - summ2)
