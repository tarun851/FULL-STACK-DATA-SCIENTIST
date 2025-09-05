a=int(input("Enter the total units comsumed:"))
if(a<=100):
    print("total amount to pay =₹",a*5,"/-")
elif(a>100 and a<=200):
    print("total amount to pay=₹",a*7,"/-")
elif(a>200):
    print("total amount to pay =₹",a*10,"/-")
else:
    print("invalid entry")

