str=input("enter space seperted marks:")
l=[int(x) for x in str.split(" ")]
a=sum(l)
percentage=(a/5)
if(percentage>=90):
   print("grade:A") 
elif(percentage>=75):
   print("grade:B") 
elif(percentage>=50):
   print("grade:C") 
elif(percentage<50):
   print("grade:Fail") 

