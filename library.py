a=int(input("Enter the total number of late days:"))
if(a>=1 and a<=5):
    print("fined with ₹10")
elif(a>=6 and a<=10):
    print("fined with ₹50")
elif(a>10):
    print("fined with ₹100")
else:
    print("invalid")