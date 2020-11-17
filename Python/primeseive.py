#prime seive computing

a=[0]*1000000

for i in range(0,1000000,2):
    a[i]=1
for i in range(3,1000000,2):
    if a[i]==1:
        for j in range(i*i,1000000,i):
            a[j]=0

a[2]=1
a[0]=a[1]=0

b=int(input("enter first number"))
c=int(input("enter second number"))

for i in range(b,c):
    if a[i]==0:
        print(i)

        
