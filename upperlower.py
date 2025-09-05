ucount,lcount=0,0
str=input("Enter a string:")
for i in str:
    if(i.isupper()):
        ucount+=1
    elif(i.islower()):
        lcount+=1
print("No of Uppercase letters:",ucount)
print("No of lowercase letters:",lcount)