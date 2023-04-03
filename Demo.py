

# print(f.read())
# f1 = open('abc.txt','a')
# f1.write("\n")
# f1.write("Glad to meet you!"
# )
# f = open('MyData.txt','r')
# f1 = open('abc.txt','w')

# for data in f:
#     f1.write(data)

f = open('IT_induction.png','rb')
f1 = open('my_pic.png','wb')

for i in f:
    f1.write(i)

