st="abbbcccaaaa"
c=1
st2=""
for i in range(0,len(st)-1):
    if(st[i]==st[i+1]):
        c=c+1
    else:
        st2+=st[i]   #ab3c3a
        print(st2)
        if(c>1):
            st2+=str(c)
            print(st2)
        c=1
st2+=st[i]
print(st2)
if(c>1):
    st2+=str(c)
    print(st2)
print(st2)

    