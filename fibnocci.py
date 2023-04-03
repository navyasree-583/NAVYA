n_terms=int(input("enter the nth term"))

n_1=0
n_2=1  
c=0

if n_terms<=0:
    print("enter a positive number")
    
elif n_terms==1:
    print(n_1)
    
else:
    while(c<n_terms):
        print(n_1)
        nth=n_1+n_2
        n_1=n_2
        n_2=nth
        c+=1
    
