l=[]
num= int(input("enter the number : "))
for i in range(0,num):
    l.append(int(input(f"Enter number at {i} index : ")))

print(f"The list of length {num} is ",l)

# print("Largest element of list is ",max(l))
# large=max(l)
# l.remove(large)
# print("Second Largest element of list is ",max(l))
# print("Smallest element of list is ",min(l))

#using sort
# l.sort()
# print("The 1st largest element is ",l[-1])
# print("The 2nd largest element is ",l[-2])
# print("The 3rd largest element is ",l[-3])

max=l[0]

for i in range(1,num):
    if(l[i]>max):
        max=l[i]
print("Largest element is ",max)