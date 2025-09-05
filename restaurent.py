a=int(input("Enter the total bill amount:"))
if(a<500):
    print("The tip to be added:",a*0.05)
elif(a>=500 and a<=1000):
    print("The tip to be added:",a*0.1)
elif(a>1000):
    print("The tip to be added:",a*0.15)

