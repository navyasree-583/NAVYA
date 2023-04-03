str1="a4b6"
num=[]
st=[]
for i in range(len(str1)):
    if i%2:
        num.append(str1[i])
    else:
        st.append(str1[i])
        
for i in range(0,len(num)):
    for k in range(0,int(num[i])):
        print(st[i])
    print(" ")