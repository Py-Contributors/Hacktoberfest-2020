## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())

a=1
b=0
i=1
while i<=n:
    c=a+b
    a=b
    b=c
    i=i+1
print(c)
    