a=int(input())
v=c=a
sum=0
count=0
while(a):
    a=a//10
    count+=1
while(c):
    d=c%10
    sum+=d**count
    c=c//10
if(v==sum):
    print("armstrong")
else:
    print("not an armstrong")