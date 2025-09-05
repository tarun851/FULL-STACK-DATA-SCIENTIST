a=0
b=1

n=int(input("enter the number to generate the sequence:"))
if(n>=1):
    print(a,end=" ")
if(n>=2):
    print(b,end=" ")
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")