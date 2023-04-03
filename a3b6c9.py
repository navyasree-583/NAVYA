""" Given a string a3b6c9 print aaabbbbbbccccccccc"""

st="a3b6c9"

s=[]
n=[]
for i in range(0,len(st)):
    if i%2==0:
        s.append(st[i])
    else:
        n.append(st[i])

print("s=",s)
print("n=",n)

for i in range(0,len(s)):
    for j in range(0,int(n[i])):
        print(s[i])
    print(" ")
