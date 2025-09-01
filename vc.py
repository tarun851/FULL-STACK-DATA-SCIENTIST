a=input()
vcount=0
ccount=0
for i in a:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vcount+=1
    else:
        ccount+=1
print("vowels=",vcount,",consonants=",ccount)